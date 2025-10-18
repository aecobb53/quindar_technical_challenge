from fastapi import FastAPI, Request, UploadFile

app = FastAPI()

# Root
@app.get('/', status_code=200)
async def root(request: Request):
    return {"Hello": "World"}

# Aggregate Metrics
@app.post('/aggregate-metrics', status_code=200)
# async def aggregate_metrics(file: UploadFile, request: Request):
async def aggregate_metrics(request: Request):
    return {"Hello": "World"}
