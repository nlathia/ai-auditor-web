import os
from flask import Flask
from src.data import db
from src.handlers import get_index, post_audit

app = Flask(__name__)

uri = os.getenv("DATABASE_URL") 
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = os.path.join(uri, "ai-audit")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.add_url_rule("/", view_func=get_index, methods=["GET"])
app.add_url_rule("/audit", view_func=post_audit, methods=["POST"])
