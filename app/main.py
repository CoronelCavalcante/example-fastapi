from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins =["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

#my_posts =[{"title": "title of post 1", "content": "contente of post one", "id": 1}, {"title": "comidinhas", "content": "coxinhas com queijo", "id": 2}]

#@app.get("/sqlalchemy")
#def test_posts(db: Session = Depends(get_db)):
#    posts = db.query(models.Post).all()
 #   return{"data": posts}




