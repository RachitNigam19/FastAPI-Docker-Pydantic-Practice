from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class royalenfield(BaseModel):
              bike_name: Annotated[str, Field(max_length=15, title="Name of the bike", description="give the bike name under 15 characters")]
              linkdein: AnyUrl
              bike_model_year: Annotated[int, Field(gt=2020, lt=2025)]
              email: EmailStr
              age: Annotated[float, Field(strict=True)]
              bike_rto: Optional[str] = None
              married: Annotated[str, Field(default=None, description="is the person married or not ")] # default value
              bike_no: str
              brand_5_name_bike: Annotated[Optional[List[str]], Field(default=None, max_length=3)]
              contact_details: Dict[str,str]


def insert(royalenfield: royalenfield):
        print(royalenfield.bike_name)
        print(royalenfield.bike_model_year)
        print(royalenfield.bike_no)
        print(royalenfield.bike_rto)
        print(royalenfield.brand_5_name_bike)
        print(royalenfield.contact_details)
        print(royalenfield.married)
        print('inserted')

bike = {
    "bike_name": "Classic350",   # under 15 chars
    "linkdein": "https://www.linkedin.com/in/rachit", 
    "bike_model_year": "2023",   # between 2020 and 2025
    "email": "rachitn46@gmail.com",
    "age": 250,
    "bike_rto": "UP14", 
    "married": "No",             # default None, yaha dummy value
    "bike_no": "UP14AB4990",
    "brand_5_name_bike": ["Meteor", "Bullet", "Hunter"],  # max 3 list items
    "contact_details": {
        "mobile": "9586419028",
        "alt_mobile": "9876543210",
        "address": "Ghaziabad, UP"
    }
}

bikes = royalenfield(**bike)

insert(bikes)
