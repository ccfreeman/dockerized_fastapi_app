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


class DriverModel(BaseModel):
    """
    Represents a driver
    """
    initial_depot: str
    final_depot: str
    final_depot_open: bool
    reefer: bool
    team: bool
    capacity: int
    changed_clock: bool
    used_duty_time: int
    used_driving_time: int
    available_time: str
    available_city: str
    available_state: str
    last_load_served_load_id: str
    last_load_served_stop_type: str


class MilesBand(BaseModel):
    """
    Miles Band
    """
    id: int
    miles_band: int
    cpm_v_single_driver: int
    cpm_r_single_driver: int
    cpm_v_team_driver: int
    cpm_r_team_driver: int


class DataModel(BaseModel):
    """
    data encapsulation
    """
    drivers: List[DriverModel]
    primary_optimization: bool
    reopt_same_day: bool
    reoptimization: bool
    excluded_load_ids: List[int]
    exclude_island_loads: bool
    carrier_code: str
    fuel_cost: float
    miles_band: List[MilesBand]
    maximum_dead_head: int
    maximum_dead_head_between_loads: int
    start_day_of_week: str
    end_day_of_week: str


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
            if data.drivers is None or len(data.drivers):
                raise ValueError("Drivers is null or empty.")
            if data.primary_optimization is None:
                raise ValueError("primary_optimization is null or empty.")


def validate_drivers():
    pass