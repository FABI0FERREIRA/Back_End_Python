from typing import Dict, Tuple, List
from sqlite3 import Connection 

class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
          self.__conn = conn

    def  registry_email(self, email_infos: Dict) -> None:
          cursor = self.__conn.cursor()
          cursor.execute(
            '''                 
                ISERT INTO emails_to_invite
                    (id, trip_id, email)
                VALUES
                    (?, ?, ?)

            ''', ( 
                 emails_to_invite["id"],
                 emails_to_invite["trip_id"],
                 emails_to_invite["email"],


            )
          )
          self.__conn.commit()
    
    def find_email_from_trip(self, trip_id: str) -> List[Tuple]: 
         cursor = self.__conn.cursor()
         cursor.execute(
             '''SELECT * FROM emails_to_invite WHERE trip_id = ? ''' (trip_id,)
         ) 
         trip = cursor.fetchone()
         return trip
