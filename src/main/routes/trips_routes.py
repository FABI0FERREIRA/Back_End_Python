from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint("trips_routes", __name__)

#importação  de controllers

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.trip_creator import LinkCreator 
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer



from src.controllers.activity_creator import AtivityRCreator 
from src.controllers.activity_finder import ActivityFinder

#importação  de Repositorios

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repositories import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitesRepository


# importanndo o gerente de conexão
from src.models.settings.db_connection_handler import db_connection_handler

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repsitory = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"], response["startus_code"]) , 200

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.gut_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirme", methods=["GET"])
def confirm_tip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    reponse = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    Participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participants_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activites", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitesRepository(conn)
    controller = ActivityCreator(activities_repository)


    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitesRepository(conn)
    controller = ActivityFinder(activities_repository)

    response = controller.find_from_trip(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/participants/<participantId>/confirme", methods=["PATH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = TripsRepository(conn)
    controller = ParticipantConfirmer(participants_repository)

    reponse = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]