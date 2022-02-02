
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

items = []

db = SQLAlchemy()

class Notes(db.Model):
    id = db.Column('id', db.String(191), primary_key=True)
    done = db.Column(db.Boolean)
    name = db.Column(db.String(225))
    created = db.Column(db.DateTime)

    def __init__(self, name, done):
        self.id = str(uuid.uuid4())
        self.name = name
        self.done = done
        self.created = datetime.now()

    def serialize(self):
        return {"id": self.id,
                "name": self.name,
                "done": self.done}