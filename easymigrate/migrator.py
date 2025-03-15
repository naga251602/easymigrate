from sqlalchemy import MetaData, Table
import sys
from easymigrate.database import create_connection


def migrate_schema_and_data(source_url, target_url):
    """Migrates schema and data from source to target database."""
    source_engine, source_conn = create_connection(source_url)
    target_engine, target_conn = create_connection(target_url)

    metadata = MetaData()
    metadata.reflect(bind=source_engine)

    for table in metadata.sorted_tables:
        print(f"Migrating table: {table.name}")

        # Create table in target DB
        table.create(target_engine, checkfirst=True)

        # Copy data
        rows = source_conn.execute(table.select()).fetchall()
        if rows:
            target_conn.execute(table.insert(), rows)
    print("\n--- Migration Completed Successfully! ---\n")

    source_conn.close()
    target_conn.close()
