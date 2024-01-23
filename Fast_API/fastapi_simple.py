#Moduled required
import uvicorn
from fastapi import FastAPI


#Creating API object
fastapi_obj=FastAPI()

#setting the route
@fastapi_obj.get('/')
def index():
    return {'message':'Hello ppl'}

@fastapi_obj.get('/Welcome')
def get_name(name: str):
    return {f'Welcome to my API development practice{name}'}

#run the api with uvicorn

if __name__ == "__main__":
    uvicorn.run(fastapi_obj,host='127.0.0.1',port=8000)