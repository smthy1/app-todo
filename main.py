from fastapi import FastAPI
from pydantic import BaseModel
from database import insert, list_all, search_by_name, complete, create_table, del_by_name

app = FastAPI()

class Item(BaseModel):
    title: str


@app.on_event("startup")
async def startup_event():
    await create_table()

#Insert new task
@app.post("/todo")
async def insert_todo(item: Item):
    await insert(item.title)
    return {"msg": "Tarefa criada."}

#Get all tasks
@app.get("/todo")
async def all_tasks():
    res = await list_all()
    return {"tasks": res}

#Get task by name
@app.get("/todo/{task_title}")
async def search_by_title(task_title: str):
    res = await search_by_name(task_title)
    return {"results": res}

#Mark as completed
@app.put("/todo/{task_title}")
async def complete_task(task_title: str):
    await complete(task_title)
    return {"msg": f"Tarefa {task_title.capitalize()} marcada como concluída."}

#Delete by task title
@app.delete("/todo/{task_title}")
async def del_task(task_title: str):
    await del_by_name(task_title)
    return {"msg": f"Tarefa '{task_title.capitalize()}' deletada."}