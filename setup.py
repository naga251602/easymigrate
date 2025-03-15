from setuptools import setup, find_packages

setup(
    name="db_migrator",
    version="1.0",
    packages=find_packages(),
    install_requires=["sqlalchemy"],
    entry_points={
        "console_scripts": ["db-migrator=db_migrator.cli:main"]
    },
    author="Your Name",
    description="A universal database migration tool",
)
