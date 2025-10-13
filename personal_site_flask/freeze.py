from app import app  # your Flask app object
from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
