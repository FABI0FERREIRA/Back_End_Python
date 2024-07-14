import uuid
from typing import Dict


class AtivityRCreator:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository


    def create(self, body, trip_id) -> Dict:
        try:
            id = str(uuid.uuid4())
            activities_info = {
                "id": id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body{"occurs_at"} 
            }
            self.__activities_repository.registry_activity(activities_info)
            return{
                "body": { "activityId": Id },
                "status_code": 201
            }
        except Exception as exeption:
            return {
                "body": {"error": "Bad Request", "message": str(exeption) },
                "status_code": 400
            }