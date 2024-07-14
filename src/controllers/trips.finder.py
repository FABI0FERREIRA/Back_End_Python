from typing import Dict

class TripFinder:
    def __init__(self, trips_repository) -> None:
        self.__trip_repository = trips_repository

    def find_trip_details(self, trip_is) -> Dict:
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_is)
            if not trip: raise Exception("No Trip Found")

            return {
                "body" : {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_ate": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6]
                    }
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body" : {"error" : "Bad Request", "message" : str(exception)},
                "status_code": 400
            }