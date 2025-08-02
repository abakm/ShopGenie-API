from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from graph import llm
from common import query_db
from models import ComparisonTemplate

prompt_template ="""
You are a professional product analyst. Create a comprehensive comparison of the product_data provided.

### Task:
Analyze the product data (extracted using ProductTemplate format) and create structured comparisons.

### Instructions:

1. **List of Products for Comparison (`comparisons`):**
   -For each product, create a comparison entry:**
   - **product_name**: Use the 'title' field
   - **brand**: Use the 'brand' field or extract from title
   - **price_range**: Use the 'price_range' field
   - **key_specs**: Extract important specifications from 'highlights' or 'content'
   - **ratings**: Create ratings based on 'score' and content analysis:
     - overall_rating: Convert 'score' to 0-5 scale (if score is 0-10, divide by 2)
     - performance: Estimate based on pros and content
     - value_for_money: Consider price vs features
   - **pros**: Use the existing 'pros' list
   - **cons**: Use the existing 'cons' list  
   - **summary**: Enhance the 'content' field with key insights

2. **Best Product Selection (`best_product`):**
   - Choose based on overall ratings, features, and value
   - Provide clear justification referencing specific strengths

### Product Data:
{product_data}

{format_instructions}
"""


def comparison_node(state):
    comparison = dict(comparisons=dict(), best_product=dict())
    products = state.get("products")
    if products:
        query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": f"Product comparison in progress"}})
        parser = JsonOutputParser(pydantic_object=ComparisonTemplate)
        format_instructions = parser.get_format_instructions()

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["product_data"],
            partial_variables={"format_instructions": format_instructions}
        )
        chain = prompt | llm | parser  # Invokes LLM with the prepared prompt
        base_prompt_tokens = len(prompt_template) + len(format_instructions)
        character_length = (5000 - base_prompt_tokens) * 4
        response = chain.invoke({"product_data": products[:character_length]})
        comparisons = response.get('comparisons')
        best_product = response.get('best_product')
        print("comparisons: ", comparisons)
        print('best_product: ', best_product)
        if best_product:
            comparison['best_product'] = best_product

        if comparisons:
            comparison['comparisons'] = comparisons

    print("COMPARISON :", comparison)
    return comparison
