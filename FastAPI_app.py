'''fastapi	The main web framework for APIs
uvicorn	ASGI server to run FastAPI apps fast'''
from fastapi import FastAPI   #Import FastAPI

app = FastAPI()   #Create a FastAPI application instance
# This 'app' object will handle all incoming HTTP requests and route them to the correct function

# Sample data
weather_data = {
    "Delhi": {"temp": 36},
    "Mumbai": {"temp": 28},
    "Bhopal": {"temp": 34}
}

@app.get("/")      #Create a root endpoint ("/")
# This endpoint is used as the home or welcome page of your API
def read_root():
    return {"message": "🏠 Welcome to the FastAPI Weather API!"}   ## When someone visits the root URL, they'll see this welcome message

@app.get("/weather/{city}")            #Create a dynamic weather endpoint ("/weather/{city}")
# The {city} part is a path parameter. Whatever city name the user provides will be passed into this function.
async def read_weather(city: str):    #endpoint to handle get request
    city = city.capitalize()
    if city in weather_data:
        return {city: weather_data[city]}
    return {"error": "City not found"}

# for run go to below in terminal 
'''uvicorn filename:app --reload'''

