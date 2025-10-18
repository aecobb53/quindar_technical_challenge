from pandas import pd
from pydantic import BaseModel


class Telemeter(BaseModel):
    name: str
    data_type: str
    nominal_limit_low: float  # These are the average values down to - the standard deviation
    nominal_limit_high: float  # These are the average values up to + the standard deviation
    critical_limit_low: float | None = None  # These are below the average values - the standard deviation
    critical_limit_high: float | None = None  # These are above the average values + the standard deviation


class AggregateMetric(BaseModel):
    station_id: str
    contact_count: int = 0
    total_bytes_received: int = 0
    total_bytes_sent: int = 0
    average_bytes_received: float = 0.0
    average_bytes_sent: float = 0.0
    total_missed_bytes: int = 0
    average_missed_bytes: float = 0.0

    @property
    def healthy(self):
        return True

    @classmethod
    def load_station(cls, data: dict):
        pass
