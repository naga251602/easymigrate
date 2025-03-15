from sqlalchemy import create_engine
import sys


def create_connection(db_url):
    """Establishes a connection to the database."""
    try:
        engine = create_engine(db_url)
        connection = engine.connect()
        print(f"Connected to {db_url} successfully!")
        return engine, connection
    except Exception as e:
        print(f"Failed to connect: {e}")
        sys.exit(1)
