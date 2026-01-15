# Threat Analysis Microservice

Eliezer Yaakovson
206568107
Negev

## Overview
This service processes CSV files containing threat data. It ranks threats based on a danger rating and stores the results in MongoDB.

## How to run
Follow the instructions in the `commands.txt` file.

## Requirements
- Python
- FastAPI
- Pandas
- Pydantic
- pymongo
- python-multipart
- uvicorn

## API endpoint
## POST
- Request: with CSV file
- Response: JSON with top 5 threats