from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns a welcome message.
    """
    return {"message": "Welcome to the Developer Snapshot API"}
