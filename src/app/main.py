from flask import Flask
from src.app.routes import api
from src.database.db import init_db

app = Flask(__name__)
app.register_blueprint(api)

@app.before_first_request
def initialize():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
