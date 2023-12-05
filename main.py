from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def f_index():
    return {"message": "Латышев Артём Романович"}

@app.get("/users")
async def f_indexT():
    return {"message": "Латышев Артём Романович"}

@app.get("/tools")
async def f_indexT():
    return {"message": "Латышев Артём Романович"}
