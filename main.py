from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


users_db = []


@app.post("/users/", response_model=User)
async def create_user(user: User):
    users_db.append(user)
    return user


@app.get("/users/", response_model=List[User])
async def read_users():
    return users_db


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    if 0 <= user_id < len(users_db):
        return users_db[user_id]
    return None


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    if 0 <= user_id < len(users_db):
        users_db[user_id] = user
        return user
    return None


@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    if 0 <= user_id < len(users_db):
        deleted_user = users_db.pop(user_id)
        return deleted_user
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
