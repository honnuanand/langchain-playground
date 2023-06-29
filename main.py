from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import translate_apis
import chatx_apis
class MyApp:
    def __init__(self):
        self.app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]


# create an instance of the MyApp class
app_instance = MyApp()
app = app_instance.app

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(translate_apis.router)
app.include_router(chatx_apis.router)
