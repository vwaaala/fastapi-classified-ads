import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Auth import AuthRouter
from Car import PersonalCarRouter
from Products import ProductsRouter
from Dashboard import DashBoardRouter
from Image import ImageRouter
from Machinery import MachineryRouter
from Truck import TruckRouter
from Upload import UploadRouter
from User import UserRouter
from WishList import WishListRouter
# from ProductsGroup import ProductsGroupRouter
from MasterData import MasterDataRouter

app = FastAPI(
    title="SuperCar Backend API",
    version="0.0.1"
)
app.include_router(DashBoardRouter.router)
app.include_router(AuthRouter.router)
app.include_router(UserRouter.router)
app.include_router(PersonalCarRouter.router)
app.include_router(ProductsRouter.router)
app.include_router(UploadRouter.router)
app.include_router(ImageRouter.router)
app.include_router(MachineryRouter.router)
app.include_router(TruckRouter.router)
app.include_router(WishListRouter.router)
app.include_router(MasterDataRouter.router)

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
    #uvicorn.run(app)
    uvicorn.run("main:app", reload=True)
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn.run(app, workers=4)
