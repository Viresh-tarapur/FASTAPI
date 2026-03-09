from fastapi import FastAPI, Path, Query, HTTPException
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

@app.get("/sort")
def sort_patients(sort_by: str = Query( ... , description='Sort on the basis of height, weight or bmi'), order: str = Query('asc',description='sort in asc or desc order')):
    
    valied_data=["height" , "weight" , "bmi"]
    if sort_by not in valied_data:
        raise HTTPException(status_code=400, detail=f"enter the this only{valied_data}")
    
    order_valied=["asc" ,"desc"]
    
    if order not in order_valied:
        raise HTTPException(status_code=400 , detail = f"enter the {order_valied}")
    
    data =dataload()
    
    sort_order= True if order == "desc" else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    return sorted_data