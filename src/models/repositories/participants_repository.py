from sqlite3 import Connection
from typing import Dict, List, Tuple

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_paticipant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.excute(
            '''
                INSERT INTO  participants
                    (id, trip_id, email_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?, ?)
            ''' ,(
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["email_to_invite_id"],
                participant_infos["name"],

            )
        
        ) 
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                from participants as p
                JOIN emails_to_ivite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.excute(
            '''
                UPDATE participants
                    SET is_confirmed = 1
                WHERE
                    id = ?
            ''', (participant_id,)
        )
        self.__conn.commit()