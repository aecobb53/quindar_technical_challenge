from fastapi import FastAPI, Response, UploadFile

from handlers import AggregateMetricsHandler

"""
This is the main app runner. It uses FastAPI. I created a simple endpoint to ensure communication `/`.
I also created the `/aggregate-metrics` endpoint to handle the CSV upload and return the aggregated metrics.
There is some basic error handling in place in the `/aggregate-metrics` endpoint.
"""

app = FastAPI()

# Root
@app.get('/', status_code=200)
async def root():
    return {"Hello": "World"}

# Aggregate Metrics
@app.post('/aggregate-metrics', status_code=200)
async def aggregate_metrics(file: UploadFile, response: Response):
    """
    Aggregate metrics from a CSV file.
    Returns a JSON object with aggregated metrics per station.
    """
    handler = AggregateMetricsHandler()

    try:
        output = await handler.aggregate_metrics(file)
    except Exception as e:
        # I would prefer to have more specific error handling here, but time prevented it
        response.status_code = 400
        return {"error": str(e)}
    return output
