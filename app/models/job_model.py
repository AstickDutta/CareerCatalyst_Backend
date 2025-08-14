from datetime import datetime
from sqlalchemy import CheckConstraint
from .. import db

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    salary_range = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Foreign Key to User
    posted_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationship
    employer = db.relationship(
        "User",
        back_populates="posted_jobs",
        foreign_keys=[posted_by]
        )
    
    applications = db.relationship(
        "Application", 
        back_populates="job", 
        lazy="dynamic", 
        cascade="all, delete-orphan"
        )

    def __repr__(self):
        return f"<Job id={self.id} title={self.title} posted_by={self.posted_by}>"
