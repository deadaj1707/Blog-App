from fastapi import APIRouter, Request, Form
from modules.note import Note
from typing import Union
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bson import ObjectId

note = APIRouter()
note.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", ""),
            "desc": doc.get("desc", ""),
            "important": doc.get("important", False),
            "likes": doc.get("likes", 0)
        })
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "newDocs": newDocs}
    )


@note.post("/", response_class=RedirectResponse)
async def create_note(
    request: Request,
    title: str = Form(...),
    desc: str = Form(...),
    important: Union[bool, None] = Form(False)
):
    new_note = {
        "title": title,
        "desc": desc,
        "important": important,
        "likes": 0
    }
    conn.notes.notes.insert_one(new_note)
    return RedirectResponse(url="/", status_code=303)


@note.post("/like/{id}", response_class=RedirectResponse)
async def like_note(
    request: Request,
    id: str
):
    conn.notes.notes.update_one({"_id": ObjectId(id)}, {"$inc": {"likes": 1}})
    return RedirectResponse(url="/", status_code=303)


@note.put("/update/{id}", response_class=RedirectResponse)
async def update_note(
    request: Request,
    id: str,
    title: str = Form(...),
    desc: str = Form(...),
    important: Union[bool, None] = Form(False)
):
    updated_note = {
        "title": title,
        "desc": desc,
        "important": important
    }
    conn.notes.notes.update_one({"_id": ObjectId(id)}, {"$set": updated_note})
    return RedirectResponse(url="/", status_code=303)



@note.post("/delete/{id}", response_class=RedirectResponse)
async def delete_note(
    request: Request,
    id: str
):
    conn.notes.notes.delete_one({"_id": ObjectId(id)})
    return RedirectResponse(url="/", status_code=303)
