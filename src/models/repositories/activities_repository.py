from sqlite3 import Connection
from typing import Dict, List, Tuple

class ActivitesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activity(self, activity_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.excute(
            '''
                INSERT INTO  activities
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?, ?, ?, ?, ?)
            ''' ,(
                activity_infos["id"],
                activity_infos["trip_id"],
                activity_infos["title"],
                activity_infos["occurs_at"],

            )
        
        ) 
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__cursor()
        cursor.execute(
            '''
                SELECT *
                FROM activities 
                WHERE trip_id = ? 
            ''', (trip_id)
        )
        activites = cursor.fetchall()
        return activites
    
