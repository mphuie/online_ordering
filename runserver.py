# app as application for wsgi
from online_ordering import app as application

application.run(debug=True)