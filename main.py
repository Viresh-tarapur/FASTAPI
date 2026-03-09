from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()


def dataload():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def home():
    return {"message": "Hello welcome to the website"}


@app.get("/about")
def about():
    return {"message": "Hello I am learning FastAPI"}


@app.get("/patient_details")
def all_patient_details():
    data = dataload()
    return data

@app.get("/view_patients_details/{patient}")
def view_detiale(patient:str =Path(..., description="Enter the patient ID", example="P001")):
    
    data = dataload()
    
    if patient in data:
        return  data[patient]
    raise HTTPException(status_code=400, detail="Invalid request")
