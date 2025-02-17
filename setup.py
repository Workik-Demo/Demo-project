from setuptools import setup, find_packages

setup(
    name="commit-message-generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'flask',
        'python-dotenv',
        'sqlalchemy',
        'psycopg2-binary',
    ],
)
