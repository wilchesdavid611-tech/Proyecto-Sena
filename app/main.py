from fastapi import FastAPI


app = FastAPI(
    title="viaCol",
    description="viaCol is a web application that allows users to upload and share files securely.",
    version="1.0.0"
)

@app.get("/")
def leer_raiz():
    return {"message": "Welcome to viaCol!"}
git checkout 