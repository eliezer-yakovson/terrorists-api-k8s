from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from pymongo import MongoClient

from db import get_db
from models import Threat

app = FastAPI()
client = get_db()

@app.post("/top-threats")
async def get_top_threats(file: UploadFile = File(...)):   
    
    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid CSV file")
    
    if 'danger_rate' not in df.columns:
        raise HTTPException(status_code=422, detail="Missing danger_rate column in CSV")

    sorted_df = df.sort_values(by='danger_rate', ascending=False)
    top_threats = sorted_df.head(5).to_dict(orient='records')

    if len(top_threats) < 5:
        count = len(top_threats)
    else:
        count = 5

    response = {
        "count": count,
        "top": []
    }

    for threat in top_threats:
        validated_threat = Threat(name=threat['name'], location=threat['location'], danger_rate=threat['danger_rate'])
        response["top"].append(validated_threat.dict())
        client.top_threats.insert_one(validated_threat.dict())
    return JSONResponse(content=response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)