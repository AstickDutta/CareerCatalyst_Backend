from .. import db
from sqlalchemy import Enum
import enum
from datetime import datetime


class ApplicationStatus(enum.Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    rejected = "rejected"
    hired = "hired"


class Application(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    resume_url = db.Column(db.String(255), nullable=False)
    status = db.Column(Enum(ApplicationStatus), nullable=False, default=ApplicationStatus.applied)
    applied_at=db.Column(db.DateTime, default=datetime.utcnow)
    created_at=db.Column(db.DateTime)
    updated_at=db.Column(db.DateTime)