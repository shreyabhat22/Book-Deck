from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from fastapi.encoders import jsonable_encoder

class BookDeck(BaseModel):

    name: str
    due_date:str
    description: str

class UserDetails(BaseModel):

    name: str
    dob:str

app= FastAPI(title="Book deck")

store_bookdeck=[]# to store the books
store_user=[]#to store user details

@app.get("/")
def basic():
    return "Welcome to the book deck!"#home page

@app.post("/bookdeck")#to add book into the deck
async def create_bookdeck(bookdeck:BookDeck):
    store_bookdeck.append(bookdeck)
    return bookdeck

@app.post("/user")#to add book into the deck
async def create_user(user:UserDetails):
    store_user.append(user)
    return user

@app.get('/bookdeck',response_model=List[BookDeck])#read
async def get_all_books():
    return store_bookdeck

@app.get('/myPage')#user page
def name():
    return ("Hello Shreya!  SRN: PES2UG19EC132  Fun fact: The tiny pocket in jeans was designed to store pocket watches")

@app.get('/bookdeck/{id}')#find
async def get_bookdeck(id:int):

    try:
        return store_bookdeck[id]
    except:
        raise HTTPException(status_code=404,detail='Book not found')

@app.put('/bookdeck/{id}')#update
async def update_bookdeck(id:int, bookdeck: BookDeck):

    try:
        store_bookdeck[id]=bookdeck
        return store_bookdeck[id]
    except:
        raise HTTPException(status_code=404,detail='Book not found')

@app.delete("/bookdeck/id/{id}")#delete book
async def delete_bookdeck(id: int):

    try:
        obj=store_bookdeck[id]
        store_bookdeck.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404,detail='Book not found')
