# Pydantic is Python Dataclasses with validation, serialization and data transformation functions.

from pydantic import BaseModel  # importing pydantic
from typing import Union, Optional, List, Dict
from rich import print
from datetime import datetime


class MyFirstModel(BaseModel):  # defining basic model
    first_name: str
    last_name: str


class MySecondModel(BaseModel):
    first_name: str
    middle_name: Union[str, None] = (
        None  # This means the parameter doesn't have to be sent
    )
    title: Optional[str] = (
        None  # this means the parameter should be sent, but can be None
    )
    last_name: str


class MyThirdModel(BaseModel):
    name: Dict[str, str]
    skills: List[str]
    holidays: List[Union[str, datetime]]


validating = MyFirstModel(
    first_name="linux", last_name="dex"
)  # passing data to model MyFirstModel

print(validating)
print(validating.__dict__)  # converting the data to dictionary

# validating_second_model = MySecondModel(
#     first_name="linux", middle_name="-", title="developer", last_name="dex"
# )
validating_second_model = MySecondModel(
    first_name="linux", middle_name="-", title="full stack developer", last_name="dex"
)

print(validating_second_model.__dict__)

third_data = {
    "name": {"first_name": "John", "last_name": "Doe"},
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "holidays": ["2025-01-01", datetime(2025, 12, 25)],
}

third_model_output = MyThirdModel(**third_data)

print(third_model_output.__dict__)
