from fastapi import FastAPI


app = FastAPI()

@app.get("/")

async def main_func():
	return {"message": "Hello World!"}


@app.get("/item/{item_id}")

async def item_func(item_id: int):
	return {"item": item_id}
