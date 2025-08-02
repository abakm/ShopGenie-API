from groq import APIStatusError
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from graph import llm
from common import query_db
from models import ListProductTemplate

prompt_template = prompt_template = """
You are a professional product analyst tasked with extracting structured information from web content about products.

### Instructions:
1. **Product Analysis**: For each product mentioned in the search contents, extract detailed information including:
   - `title`: The product name/model (required)
   - `url`: Source URL of the information
   - `content`: Concise summary of the product's main features and purpose
   - `pros`: List of positive aspects, advantages, or strengths
   - `cons`: List of negative aspects, disadvantages, or limitations
   - `highlights`: Dictionary of notable features, specifications, or key differentiators
   - `score`: Numerical rating if available (0.0-10.0 scale), otherwise null
   - `price_range`: Price information if mentioned (e.g., "$100-200", "Under $500")
   - `brand`: Product brand or manufacturer
   - `category`: Specific subcategory or product type

2. **Quality Guidelines**:
   - Only extract products with substantial information available
   - Ensure pros and cons are factual and specific to the product
   - Highlights should contain key specifications, features, or selling points
   - Maintain objectivity and accuracy in all extracted information
   - If information is not available, use null rather than making assumptions

3. **Output Requirements**:
   - Extract at least 1 product if any meaningful product information exists
   - Focus on products that have enough detail for comparison
   - Prioritize recent and comprehensive product information

### Search Contents:
{search_contents}

{format_instructions}"""

def extraction_node(state):
    products = list()
    search_contents = state.get("search_contents")
    query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": f"Extraction neccessary data"}})
    if search_contents:
        query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": f"Extraction neccessary data"}})
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
        try:
            response = chain.invoke({"search_contents": search_contents})
            products = response.get("products")

            if not products or not len(products) > 1:
                query_db.update_one({"_id": state["query_id"]}, {"$set":
                                                                     {"status": "Unable to extraction required information"
                                                                      }
                                                                 })
                products = list()

        except (APIStatusError, OutputParserException) as err:
            query_db.update_one({"_id": state["query_id"]}, {"$set":
                                                                 {"status":
                                                                      f"Unable to extraction required information:{err}"
                                                                  }
                                                             })
    return dict(products=products)



