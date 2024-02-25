# FastAPI Courier Tracking System

## Overview

This is a FastAPI-based Courier Tracking System that allows users to create couriers, retrieve their current locations, and update their locations dynamically.

## Features

* Create Courier: Allows users to create a new courier with a specified name and initial location.
* Get Courier Location: Retrieves the current location of a courier based on their ID.
* Change Courier Location: Updates the location of a courier dynamically.

## Installation

* Clone the repository:
```bash
git clone https://github.com/yabanci/cc_back
```

* Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

* Start the FastAPI server:
```bash
python3 main.py
```

* Use the provided API endpoints to interact with the Courier Tracking System.
API Endpoints

    * POST `/couriers`: Create a new courier.
    * GET `/couriers`: Retrieve the location of a courier.
    * POST `/couriers/{courier_id}/location`: Update the location of a courier.

## Example Usage

* Creating a courier:
```bash
curl -X POST "http://localhost:8000/couriers" -H "Content-Type: application/json" -d '{"name": "John Doe", "location": {"latitude": 51.123, "longitude": 71.456}}'
```

* Retrieving courier location:
```bash
curl -X GET "http://localhost:8000/couriers/1"
```

* Updating courier location:
```bash
curl -X POST "http://localhost:8000/couriers/1/location" -H "Content-Type: application/json" -d '{"latitude": 51.234, "longitude": 71.789}'
```