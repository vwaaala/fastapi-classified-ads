import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from User.UserRouter import router as UserRouter

app = FastAPI(
    title="SuperCar Backend API",
    version="0.0.1"
)
app.include_router(UserRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"version": "v1.0.0"}


if __name__ == '__main__':
    # from app.database import Base, engine
    # Base.metadata.create_all(bind=engine)
    # uvicorn.run(app)
    uvicorn.run("main:app", reload=True)
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn.run(app, workers=4)
