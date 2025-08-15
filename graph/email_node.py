import os
from ssl import SSLError
from socket import error
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from graph import llm
from models import State, EmailRecommendation

SERVER = "smtp.gmail.com"
PORT = 587
MAIL = os.getenv("EMAIL_USERNAME", "akhilakmgb@gmail.com")
PASSWORD = os.getenv("EMAIL_PASSWORD", "cqcc lhus jlnd ouii")

email_html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Email Recommendation</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f8f8f8;
      margin: 0;
      padding: 0;
    }}
    .container {{
      max-width: 600px;
      margin: 20px auto;
      background-color: #ffffff;
      padding: 20px;
      border-radius: 8px;
      color: #333333;
    }}
    h1 {{
      color: #4a90e2;
    }}
    .button {{
      display: inline-block;
      background-color: #4a90e2;
      color: white !important;
      text-decoration: none;
      padding: 12px 20px;
      border-radius: 5px;
      margin: 15px 0;
      font-weight: bold;
    }}
    .footer {{
      font-size: 12px;
      color: #999999;
      text-align: center;
      margin-top: 30px;
      border-top: 1px solid #dddddd;
      padding-top: 15px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>{heading}</h1>

    <p><strong>Our Top Pick:</strong> {product_name}</p>
    <p>{justification}</p>

    <p>Watch our in-depth review to explore why this phone is the best choice for you:</p>
    <p><a href="{youtube_link}" class="button">Watch the Review</a></p>

    <p>Want to learn more? Visit our website or follow us for more recommendations.</p>
    <p><a href="#" class="button">Explore Now</a></p>

    <div class="footer">
      &copy; 2025 ShopeGenie Recommendations, All Rights Reserved.
    </div>
  </div>
</body>
</html>
"""



email_prompt = """
You are an expert email content writer.

Generate an email recommendation based on the following inputs:
- Product Name: {product_name}
- Justification: {justification}
- Query: "{query}" (a general idea of the user's interest).

Return your output in the following JSON format:
{format_instructions}

### Input Example:
Product Name: Google Pixel 8 Pro
Justification: Praised for its exceptional camera, advanced AI capabilities, and vibrant display.
Query: a phone with an amazing camera

### Example Output:
{{
  "subject": "Capture Every Moment with Google Pixel 8 Pro",
  "heading": "Discover the Power of the Ultimate Photography Smartphone",
  "justification": "Known for its exceptional camera quality, cutting-edge AI features, and vibrant display, the Google Pixel 8 Pro is perfect for photography enthusiasts."
}}

Now generate the email recommendation based on the inputs provided.
"""


def email_node(state: State):
    best_product = state.get('best_product')
    if best_product:
        user_query = state["query"]
        best_product_name = best_product["product_name"]
        justification = best_product["justification"]
        youtube_link = state["youtube_link"]
        parser = JsonOutputParser(pydantic_object=EmailRecommendation)
        prompt = PromptTemplate(
            template=email_prompt,
            input_variables=["product_name", "justification", "query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        chain = prompt | llm | parser
        try:
            response = chain.invoke(
                dict(product_name=best_product_name, justification=justification, query=user_query))
            html_content = email_html_template.format(
                product_name=best_product_name,
                justification=response["justification"],
                youtube_link=youtube_link,
                heading=response['heading']
            )
            subject = response['subject']
        except OutputParserException:
            html_content = email_html_template.format(
                product_name=best_product_name,
                justification=justification,
                youtube_link=youtube_link,
                heading=f"ShopGenie Recommendation for the query: {state['query']}"
            )
            subject = "ShopGenie Recommendations"


        try:
            # Create email content
            message = MIMEMultipart()
            message['From'] = MAIL
            message['To'] = state['email']
            message['Subject'] = subject

            # Add the email body
            message.attach(MIMEText(html_content, 'html'))

            # Connect to the SMTP server
            with SMTP(SERVER, PORT) as server:
                server.starttls()  # Start TLS encryption
                server.login(MAIL, PASSWORD)  # Login to the server
                server.send_message(message)  # Send the email
                print(f"Email sent successfully to {state['email']}.")

        except (SMTPException, error, SSLError, OSError) as err:
            print(f"Failed to send email: {err}")
