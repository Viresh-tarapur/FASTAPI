# FastAPI Patient API

This is a simple FastAPI backend project that reads patient data from a JSON file and provides REST API endpoints.

## Features
- FastAPI backend
- JSON based data storage
- Simple REST API

## Endpoints

### Home
GET /

Returns welcome message.

### View Patients
GET /view

Returns all patient data from `patients.json`.

## Tech Stack
- Python
- FastAPI
- JSON

## Run the Project

Install dependencies:

pip install fastapi uvicorn

Run server:

uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000/docs
