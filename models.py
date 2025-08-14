from typing import List, Optional, Dict, Any, TypedDict
from pydantic import BaseModel, EmailStr, Field



# Payload Validation
class PayloadTemplate(BaseModel):
    query: str
    email: EmailStr


class ProductTemplate(BaseModel):
    """A review/analysis of any product."""
    title: str = Field(..., description="The title/name of the product")
    url: Optional[str] = Field(None, description="The URL of the product review or source")
    content: Optional[str] = Field(None, description="The main content/summary of the product")
    pros: Optional[List[str]] = Field(None, description="The advantages/positive aspects of the product")
    cons: Optional[List[str]] = Field(None, description="The disadvantages/negative aspects of the product")
    highlights: Optional[Dict[str, Any]] = Field(None, description="Key features, specifications, or notable aspects of the product")
    score: Optional[float] = Field(0.0, description="The rating/score of the product (0.0-10.0)")
    price_range: Optional[str] = Field(None, description="Price range or cost information")
    brand: Optional[str] = Field(None, description="Brand or manufacturer of the product")
    category: Optional[str] = Field(None, description="Product category or type")


class ListProductTemplate(BaseModel):
    """A list of product reviews/analyses."""
    products: List[ProductTemplate] = Field(..., description="List of individual product reviews/analyses")


class SimpleRatings(BaseModel):
    """Simple ratings structure."""
    overall_rating: float = Field(..., description="Overall rating out of 5")
    performance: float = Field(..., description="Performance rating out of 5")
    value_for_money: float = Field(..., description="Value rating out of 5")


class SimpleComparison(BaseModel):
    """Simple product comparison."""
    product_name: str = Field(..., description="Product name")
    brand: str = Field(..., description="Brand name")
    price_range: str = Field(..., description="Price range")
    key_specs: Dict[str, str] = Field(..., description="Key specifications")
    ratings: SimpleRatings = Field(..., description="Product ratings")
    pros: List[str] = Field(..., description="Product advantages")
    cons: List[str] = Field(..., description="Product disadvantages")
    summary: str = Field(..., description="Product summary")


class BestProductSelection(BaseModel):
    """Best product selection."""
    product_name: str = Field(..., description="Best product name")
    justification: str = Field(..., description="Why this product is best")


class ComparisonTemplate(BaseModel):
    """Complete comparison result."""
    comparisons: List[SimpleComparison] = Field(..., description="Product comparisons")
    best_product: BestProductSelection = Field(..., description="Best product selection")


class EmailRecommendation(BaseModel):
    subject: str = Field(..., description="The email subject line, designed to capture the recipient's attention.")
    heading: str = Field(..., description="The main heading of the email, introducing the recommended product.")
    justification: str = Field(..., description="A concise explanation of why the product is being recommended.")


class State(TypedDict):
    query_id:int
    query: str
    email: str
    search_contents: list
    products: list[ListProductTemplate]
    comparisons: list[ComparisonTemplate]
    best_product: dict
    youtube_link: str
