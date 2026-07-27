from sqlalchemy import text

from app.database.connection import engine


def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.scalar()

            print("✅ Successfully connected to PostgreSQL!")
            print(version)

    except Exception as e:
        print("❌ Connection failed!")
        print(e)


if __name__ == "__main__":
    test_connection()