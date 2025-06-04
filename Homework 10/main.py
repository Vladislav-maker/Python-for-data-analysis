import joblib
import uvicorn

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()



with open("model.pkl", 'rb') as file:
    model = joblib.load(file)


class ModelRequestData(BaseModel):
    total_square: float
    rooms: float


class Result(BaseModel):
    result: float


@app.get("/health")
def health():
    return JSONResponse(content={"message": "It's alive!"}, status_code=200)


@app.get("/predict_get")
def get_predict():
    return Result(result=round(predictions[0]))


@app.post("/predict_post", response_model=Result)
def preprocess_data(data: ModelRequestData):
    global predictions

    df = pd.DataFrame({
    'total_square': [data.total_square],
    'rooms': [data.rooms]  })

    predictions = model.predict(df)
    
    return Result(result=round(predictions[0]))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
