from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from common import llm
from models import ListProductTemplate

prompt_template = """
You are a professional assistant tasked with extracting structured information from blogs.

### Instructions:
1. **Product Details**: For each product in search contents, populate the `products` array with structured data for each item, including:
   - `title`: The product name.
   - `url`: Link to the blog post or relevant page.
   - `content`: A concise summary of the product's main features or purpose.
   - `pros`: A list of positive aspects or advantages of the product if available otherwise extract blog content.
   - `cons`: A list of negative aspects or disadvantages if available otherwise extract blog content.
   - `highlights`: A dictionary containing notable features or specifications if available otherwise extract blog content.
   - `score`: A numerical rating score if available; otherwise, use `0.0`.

### Search Contents:
{search_contents}

After extracting all information, just return the response in JSON format as per the schema.
"""


def extract_node(state):
    products = list()
    search_contents = state.get("search_contents")
    if search_contents:
        parser = JsonOutputParser(pydantic_object=ListProductTemplate)
        format_instructions = parser.get_format_instructions()

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["search_contents"],
            partial_variables={"format_instructions": format_instructions}
        )
        chain = prompt | llm | parser  # Invokes LLM with the prepared prompt
        base_prompt_tokens = len(prompt_template) + len(format_instructions)
        character_length = (5000 - base_prompt_tokens) * 4
        if len(search_contents) > character_length:
            search_contents = search_contents[:character_length]
        response = chain.invoke({"search_contents": search_contents})
        products = response.get("products")
        if not products or not len(products) > 1:
            products = list()

    return dict(products=products)



