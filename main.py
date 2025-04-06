from config import *

@app.get("/")
def echo():
    return JSONResponse(
        content={
            "message": "Hello World!"
        },
        status_code=200
    )