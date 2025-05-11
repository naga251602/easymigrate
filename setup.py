from setuptools import setup, find_packages

setup(
    name="easymigrate",
    version="1.0",
    packages=find_packages(),
    install_requires=["sqlalchemy"],
    entry_points={
        "console_scripts": ["easymigrate=easymigrate.cli:main"]
    },
    author="GAURAV N V",
    description="A universal database migration tool",
)
