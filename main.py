# main.py
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Load the trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the FastAPI app
app = FastAPI()

# Define the input data model
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API!"}

@app.post("/predict/")
def predict(data: IrisInput):
    # Prepare the input data
    input_data = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    # Make prediction
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
