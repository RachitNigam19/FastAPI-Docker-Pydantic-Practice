from fastapi import FastAPI, Path, Query, HTTPException
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

# pydantic mode for data validation
class patient(BaseModel):
        id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
        name: Annotated[str, Field(..., description='Name of the patient')]
        city: Annotated[str, Field(..., description='City of the Patient')]
        age: Annotated[int, Field(..., description='Age of the patient')]
        gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient', examples=['male', 'female'])]
        height: Annotated[float, Field(..., gt=0, description='Height of the patient in meters', examples=['1.78'])]
        weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in meters', examples=['82'])]

        # computation field for calculating bmi
        @computed_field
        @property
        def bmi(self) -> float:
                bmi = round(self.weight/(self.height**2), 2)
                return bmi
        
        # Computed field for calculating verdict
        @computed_field
        @property
        def verdict(self)-> str:
                bmi = self.bmi

                if bmi < 18.5:
                        return "Underweight"
                elif 18.5 <= bmi < 25:
                        return "Normal weight"
                elif 25 <= bmi < 30:
                        return "Overweight"
                elif 30 <= bmi < 35:
                        return "Obese (Class I)"
                elif 35 <= bmi < 40:
                        return "Obese (Class II)"
                else:
                        return "Obese (Class III)"
        
# class for Patient Update
class PatientUpdate(BaseModel):
        id: Annotated[Optional[str],Field(default=None)]
        name: Annotated[Optional[str],Field(default=None)]
        city: Annotated[Optional[str],Field(default=None)]
        age: Annotated[Optional[int],Field(default=None)]
        gender: Annotated[Optional[Literal ['male', 'female']],Field(default=None)]
        height: Annotated[Optional[float],Field(default=None, gt=0)]
        weight: Annotated[Optional[float],Field(default=None, gt=0)]


# Function for loading data 
def load():
        with open("patients.json", 'r') as f:
                data = json.load(f)
                return data
        
def save_data(data):
        # save updated data back to the json file
        with open('patients.json', 'w') as f:
                json.dump(data, f, indent=4)

app = FastAPI()
        
# routes
@app.get("/")
def home():
              return("Patient Management System")

@app.get("/about")
def about():
              return("This is Patient Management System API")

@app.get("/view")
def view():
              data = load()
              return data

# Path Param to view one patient
@app.get("/patients/{patient_id}")
def patientz(patient_id:str = Path(..., description="Id od the patient in the db", example='P001')):
        data = load()
        if patient_id in data:
                return data[patient_id]
        raise HTTPException(status_code=404, detail="Patient does not exist")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="sort on the basis of the height, weight or bmi"),
                  order : str = Query('asc', description= "sort in asc or dewsc order")):
        
        valid_fields = ['height', 'weight', 'bmi']

        if sort_by not in valid_fields:
                raise HTTPException(status_code=400, detail= f"invalid field selected from {valid_fields}") 

        if order not in ['asc', 'desc']:
                raise HTTPException(status_code=400, detail= f"invalid field selected from {order} select between asc or desc")

        data = load()
        sorted_order = True if order == 'desc' else False
        sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = sorted_order) 

        return sorted_data

# create operation API endpoint to create a new patient record
@app.post('/create')
def create(validator:patient):
        # load data
        data = load()
        # check if patient already exist's
        if validator.id in data:
                raise HTTPException(status_code=400, detail='patient already exists')
        
        # new patient add to the database
        data[validator.id] = validator.model_dump(exclude=['id'])

        # save into the json file 
        save_data(data)

        # returning json response 
        return JSONResponse(status_code=201, content="patient created successfully")

# API endpoint for patient details update
@app.put('/update/{Patient_id}') #adding path here patient id
def updatePatient(Patient_id:str,update:PatientUpdate): 
        # load data and check this id patient is there or  not
        data = load()
        if Patient_id not in data:
                raise HTTPException(status_code=404, detail="patient does not exist")
        
        # loading data for specific id 
        existing_patient_info = data[Patient_id]
        updated_patient_info = update.model_dump(exclude_unset=True)

        for key, value in updated_patient_info.items():
                existing_patient_info[key] = value

        existing_patient_info['id'] = Patient_id 
        existing_pydantic_object = patient(**existing_patient_info)

        existing_patient_info = existing_pydantic_object.model_dump(exclude='id')
        data[Patient_id] = existing_patient_info

        save_data(data)

        return JSONResponse(status_code=200, content="patient updates successfully")

# Delete Endpoint
@app.delete('/delete/{patient_id}')
def deletez(patient_id:str):
        data = load()
        if patient_id not in data:
                raise HTTPException(status_code=400, detail="Patient do not exists")
        del data[patient_id]

        save_data(data)

        return JSONResponse(status_code=200, content="user deleted successfully")
        



