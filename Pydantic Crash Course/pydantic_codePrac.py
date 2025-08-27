# importing dependencies
from pydantic import BaseModel, Field, AnyUrl, EmailStr, field_validator, model_validator, computed_field
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import List,Annotated, Optional

# nested models concept
# class for address
class Address(BaseModel):
        houseno: int
        street_name: str
        city:str
        state:str
        pincode: int

# pydantic model class
class patient(BaseModel):
              # variable (inputs for data) we need to validate 
              name:Annotated[str, Field(max_length=25, title="name of the patient", description="enter the patient name in 25 characters", examples=["Nitish Singh", "Rachit Nigam"], strict=True)]

              age: Annotated[float, Field(gt=0, lt=125, title="age of the patient", description= "enter the age in max 125", examples=[45, 29])]

              weight: Annotated[float, Field(gt=0, lt=500, title="weight of the patient", description= "enter the weight of the patient in max 3 digits", examples=[65,89])]

              height: Annotated[float, Field(gt=0, lt=500, title="height of the patient", description= "enter the height of the patient in max 3 digits (Centimeters)", examples=[156,189])]

              address: Address

              social_profile_url: Annotated[Optional[AnyUrl], Field(title="social profile like linkdein of the patient", description= "enter the url of the linkdein of the patient", examples=["https://chatgpt.com"])]

              email: Annotated[EmailStr, Field(title="email of the patient", description= "enter the email of the patient in max 3 digits", examples= "abc@gmail.com", strict= True)]

              mobile: Annotated[PhoneNumber, Field(title="phone number of the patient", description= "enter the phone number of the patient in max 10 digits", examples= 9586419028, strict=True)]

              allergies: Annotated[Optional[List[str]], Field(title="allergies of the patient", description= "enter the allergies of the patient in max no of allergies are 3", examples=['pollen', 'dust'])]

              married: Annotated[bool, Field(title="marital status of the patient", description= "marital status of the status", examples=['True' or 'False'])]

              # creating a method for patient class (decorator) which checks the email and then let us know that if the email of the client is icici domain or hdfc domain then only he can sign in or enter thier entry into the database other wise no entry 

              @field_validator('email')
              @classmethod
              def email_validation(cls, value):
                      valid_domains = ['icici.com', 'axis.com', 'hdfc.com']
                      domain_name = value.split('@')[-1]

                      if domain_name not in valid_domains:
                              raise ValueError("not a valid domain email address for banking")
                      else:
                              return value
              
              # creating a class method for converting the name in to caps
              @field_validator('name', mode="after")
              @classmethod
              def name_caps(cls, value):
                      return value.upper()
              
              # creating a model validation class 
              @model_validator(mode="after")
              def validate_emergency_nu(cls,model):
                      if model.age > 60 and 'emergency' not in model.allergies:
                              raise ValueError('patients older than 60 requires emergency mobile no')
                      return model
              
              # Computational model
              @computed_field
              @property
              def bmi(self) -> float:
                      bmi = round(self.weight/(self.height**2),2)
                      return bmi

# creating a insert function to insert data into database
def insert(patient:patient):
        print(patient.name)
        print(patient.age)
        print(patient.address)
        print(patient.allergies)
        print(patient.weight)
        print(patient.height)
        print(patient.email)
        print(patient.mobile)
        print(patient.married)
        print(patient.social_profile_url,"\n")
        print(patient.bmi)
        print("Inserted into database")
# Annotated[Optional[str], Field(max_length=250, title="Address of the patient", description= "enter the address of the patient in max 250 characters", default=None)]

dummy_data = {
    "houseno": 123,
    "street_name": "MG Road",
    "city": "Ghaziabad",
    "state": "Uttar Pradesh",
    "pincode": 201002
}

dummy_datas = Address(**dummy_data)
patientx = {
    "name": "Rachit Nigam",  # max 25 chars
    "age": 69,               # between 0 and 125
    "weight": 75,          # between 0 and 500
    "height": 1.75,           # between 0 and 500 (cm)
    "address": dummy_datas,  # max 250 chars
    "social_profile_url": "https://www.linkedin.com/in/rachit", 
    "email": "rachitn46@icici.com",
    "mobile": "+91 9586419028",   # using pydantic-extra-types PhoneNumber
    "allergies": ["pollen", "dust", "emergency"],  # max 3 items
    "married": True
}

patients = patient(**patientx)
# calling insert function
insert(patients)

temp = patients.model_dump(exclude='name')
print(temp)