from shuffle import app
from flask import session

if __name__ == '__main__':
    with app.test_request_context("/"):
        session["key"] = "value"
    app.run()
