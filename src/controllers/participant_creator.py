import uuid
from typing import Dict


class ParticipantCreator:
    def __init__(self, participants_repository, email_repository) -> None:
        self.__participants_repositry = participants_repository
        self.__emails_repository = emails_repository
    
    def create(self, body, trip_id) -> Dict:
        try:    
            participant_id = str(uuid.uuid4())
            emil_id = str(uuid.uuid4())
            
            email_infos = {
                "email": body{"email"},
                "id": email_id,
                "trip_id": trip_id
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "email_to_invite_id": email_id,
                "name": body["name"]

            }

            self.__emails_repository.registry_email{email_infos}
            self.__participants_repositry.registry_participant(participant_infos)
            
            return {
                    "body" : { "participant_id": participant_id }
                    "status_code": 201                 
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception) },
                "status_code": 400
            }   