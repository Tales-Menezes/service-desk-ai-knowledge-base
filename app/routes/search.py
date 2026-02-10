from flask import Blueprint, render_template, request
from app.services.query_service_factory import get_query_service

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=["GET", "POST"])
def search():
    results = []
    query = ""
    client = ""

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        client = request.form.get("client", "").strip()

        service = get_query_service()
        results = service.search(query=query, client=client or None, top=5)

    return render_template("search.html", results=results, query=query, client=client)
