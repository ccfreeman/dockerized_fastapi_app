import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from starlette.responses import RedirectResponse
from .engines.models import RequestModel, HealthCheckModel, validate_request_model

app = FastAPI()

@app.get("/")
async def home():
    """Home page for the application. Redirects to the FastAPI docs page.

    Parameters
    ----------

    Returns
    -------
    JSONResponse with a list of facilities and scores
    """
    return RedirectResponse(url='/docs')


@app.post("/match")
async def match_facilities(data: RequestModel):
    """Passes in a json array of items and returns that array.

    Parameters
    ----------
    data : RequestModel

    Returns
    -------
    JSONResponse with a list of facilities and scores
    """
    try:
        validate_request_model(data)
    except ValidationError:
        return JSONResponse(status_code=403, content={})
    return JSONResponse(status_code=201, content=data)


@app.post("/match_addresses")
async def match_addresses(data: RequestModel):
    """Passes in a json array of items and returns that array.

    Parameters
    ----------
    data : RequestModel

    Returns
    -------
    JSONResponse with a list of facilities, addresses, and scores
    """
    try:
        validate_request_model(data)
    except ValidationError:
        return JSONResponse(status_code=403, content={})
    return JSONResponse(status_code=201, content=data)


@app.get("/health", response_model=HealthCheckModel)
async def health():
    """Application health check

    Parameters
    ----------

    Returns
    -------
    JSONResponse with a list of facilities and scores
    """
    # try:
    #     pass
    # except:
    #     return JSONResponse(status_code=403, content={})
    h = HealthCheckModel(status='ok')
    json_compatible_health_data = jsonable_encoder(h)
    return JSONResponse(status_code=200, content=json_compatible_health_data)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)