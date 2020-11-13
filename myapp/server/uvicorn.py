import uvicorn


def run(host, port):
    uvicorn.run("myapp.main:app", host=host, port=port, reload=True)
