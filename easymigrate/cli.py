import sys
from db_migrator.migrator import migrate_schema_and_data


def main():
    if len(sys.argv) < 3:
        print("Usage: python -m db_migrator <source_db_url> <target_db_url>")
        sys.exit(1)

    source_db = sys.argv[1]
    target_db = sys.argv[2]
    migrate_schema_and_data(source_db, target_db)


if __name__ == "__main__":
    main()
