from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, devices, data

app = FastAPI()

# ✅ CORS middleware config
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(devices.router, prefix="/devices", tags=["Devices"])
app.include_router(data.router, prefix="/data", tags=["IoT Data"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "IoT Backend is running"}
