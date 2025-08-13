from datetime import datetime
from sqlalchemy import CheckConstraint
from .. import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="job_seeker")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    posted_jobs = db.relationship(
        "Job",
        back_populates="employer",
        lazy="dynamic",
        cascade="all, delete-orphan",
        foreign_keys="Job.posted_by"
    )

    applications = db.relationship(
        "Application",
        back_populates="applicant",
        lazy="dynamic",
        cascade="all, delete-orphan",
        foreign_keys="Application.applicant_id"
    )

    __table_args__ = (
        CheckConstraint("role in ('job_seeker','employer','admin')", name="ck_users_role"),
    )

    def __repr__(self):
        return f"<User id={self.id} email={self.email} role={self.role}>"