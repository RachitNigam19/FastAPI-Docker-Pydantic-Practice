# importing dependencies 
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
import pandas as pd
from typing import Literal, Annotated
import pickle

# loading machine learning model
with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

# fast api object 
app = FastAPI()

tier_1_cities = [
    "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"
]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# building pydantic object to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, lt=500, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=3, description='Height of the user in meters')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual income of the user in LPA')]
    smoker: Annotated[bool, Field(..., description='Is the user smoker?')]
    city: Annotated[str, Field(..., description='The city from where the user belongs to')]
    occupation: Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'],
        Field(..., description='Occupation of the user')
    ]

    # ✅ BMI property
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    # ✅ Lifestyle risk
    @property
    def life_style(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    # ✅ Age group
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    # ✅ City tier
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3


@app.post('/predict')
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.life_style,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={"predicted_category": str(prediction)})
