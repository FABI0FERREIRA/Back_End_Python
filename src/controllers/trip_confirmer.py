from typing import Dict

class TripConfirmer:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository
    
    def confirm(self, trip_id) -> Dict:
        try:
            self.__trips_repository.update_trip_status(trip_id)
            return { "body" : None, "status_code": 204 }
        