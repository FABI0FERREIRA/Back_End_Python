class LinkFinder:
    def __init__(self, link_repository) -> None:
        self.__link_repository = link_repository
    
    def find(self, triId):
        try:
            links = self.__links_repository.find_link_from_trip(triId)

            fromatted_links = []
            for link in link:
                fromatted_links.append({
                    "id" : link[0],
                    "url": link[2],
                    "title" : link[3]

                })
            return {
                "body" : { "links": fromatted_links},
                "status_code" : 200
            }

        except Exception as exception:
            return {
                "body" : { "error": "Bad Request", "massage": str(exception)},
                "status_code" : 400
            }