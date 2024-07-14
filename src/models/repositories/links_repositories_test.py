import pytest
import uuid
from .links_repositories import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()

link_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": "123-43321",
        "trip_id": trip_id,
        "link": "somelink.com",
        "title": "Hotel"

    }

    link_repository.registry_link(link_infos)

def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    response = link_repository.find_links_from_trip()
    print()
    print(response)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)

    