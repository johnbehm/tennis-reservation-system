from app.database.base import Base
from app.database.connection import engine

# Import all models so SQLAlchemy registers them.
from app.models.court import Court


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")


if __name__ == "__main__":
    create_tables()