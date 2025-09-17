from . import db

class Knowledge(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return f"<Knowledge {self.title}>"