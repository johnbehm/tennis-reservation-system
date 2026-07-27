from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.court import Court


def seed_database():
    db: Session = SessionLocal()

    try:
        if db.query(Court).count() == 0:
            courts = [
                Court(name="Court 1", surface="Hard", indoor=True),
                Court(name="Court 2", surface="Hard", indoor=True),
                Court(name="Court 3", surface="Hard", indoor=False),
                Court(name="Court 4", surface="Clay", indoor=False),
            ]

            db.add_all(courts)
            db.commit()

            print("✅ Courts added!")
        else:
            print("Database already contains courts.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()