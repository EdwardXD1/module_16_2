from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get('/user/admin')
async def admin():
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def id(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=1)) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user')
async def user_id(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                    age: int = Path(ge=18, le=120, description="Enter age", example=24)) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get('/')
async def main():
    return {'message': "Главная страница"}


#uvicorn src.main:app --reload