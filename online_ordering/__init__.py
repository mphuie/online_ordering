from flask import Flask
app = Flask(__name__)

from online_ordering.views import aview
from online_ordering.database import db_session

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()