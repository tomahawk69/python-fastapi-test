from models.globals import Version
from datetime import datetime


def enrich(input: dict, version: Version):
    input.update({"version": version, "timestamp": datetime.now()})
