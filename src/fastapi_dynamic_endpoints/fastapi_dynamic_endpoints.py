from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# This will be our dynamic endpoint function
def dynamic_hello():
    return JSONResponse({"message": "Hello, dynamic world!"})

@app.get("/")
def root():
    return {"message": "Root endpoint. Use /add or /remove to manage /dynamic."}

@app.post("/add")
def add_dynamic():
    # Add the /dynamic endpoint
    app.add_api_route("/dynamic", dynamic_hello, methods=["GET"])
    app.openapi_schema = None
    return {"status": "added"}

@app.post("/remove")
def remove_dynamic():
    app.router.routes[:] = [
        route for route in app.router.routes
        if not (getattr(route, "path", None) == "/dynamic" and "GET" in getattr(route, "methods", []))
    ]
    app.openapi_schema = None
    return {"status": "removed"}


def main():
    pass


if __name__ == "__main__":
    main()
