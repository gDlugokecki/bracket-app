"""Base schemas with camelCase conversion for API responses"""

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelCaseModel(BaseModel):
    """Base model that converts snake_case fields to camelCase in API responses"""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,  # Accept both snake_case and camelCase from client
        from_attributes=True,  # Allow creating from ORM models
    )
