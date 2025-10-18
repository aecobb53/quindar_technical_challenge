from fastapi import FastAPI, Response, UploadFile

from handlers import AggregateMetricsHandler

app = FastAPI()

# Root
@app.get('/', status_code=200)
async def root():
    return {"Hello": "World"}

# Aggregate Metrics
@app.post('/aggregate-metrics', status_code=200)
async def aggregate_metrics(file: UploadFile, response: Response):
    handler = AggregateMetricsHandler()

    try:
        output = await handler.aggregate_metrics(file)
    except Exception as e:
        response.status_code = 400
        return {"error": str(e)}
    return output
