from dotenv import load_dotenv
from neo4j import GraphDatabase, basic_auth
import os

load_dotenv()
URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PWD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(URI, auth=basic_auth(USER, PWD))

def get_session(database: str = None):
    return driver.session(database=database) if database else driver.session()

