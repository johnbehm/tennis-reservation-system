from sqlalchemy.orm import Session

from app.models.court import Court


def get_all_courts(db: Session):
    return db.query(Court).all()