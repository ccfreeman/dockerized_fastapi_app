"""
Contains models
"""
from pydantic import BaseModel
from typing import List, Optional


class HealthCheckModel(BaseModel):
    """

    """
    status: str
    error: Optional[str]


class DataModel(BaseModel):
    """
    data encapsulation
    """
    facility_name: str
    address1: str
    address2: str
    city: str
    state: str
    zipcode: str
    country: int


class RequestModel(BaseModel):
    """
    Request body
    """
    data: List[DataModel]


def validate_request_model(req: RequestModel):
    pass
    if req:
        for data in req.data:
            # testing to see if there are drivers.
            if data.address1 is None or len(data.address1):
                raise ValueError("Address1 field is null or empty.")
            if data.state is None:
                raise ValueError("State is null or empty.")
