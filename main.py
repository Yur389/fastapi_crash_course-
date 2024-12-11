from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # delet all tadles
    await delete_tables()
    print("База отщищена")
    # creation tables
    await create_tables()
    print("База готова")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
    

# tasks = []

# @app.post("/tasks")
# async def add_task(
#     task: Annotated[STaskAdd, Depends()],
# ):
#     tasks.append(task)
#     return{"ok":True}

# # @app.get("/tasks")
# # def get_tasks():
# #     task = Task(name = "Save this video")
# #     return {"date": task}

