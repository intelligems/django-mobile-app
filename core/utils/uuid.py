from uuid import uuid4


def get_fresh_uuid():
    return str(uuid4()).replace('-', '')
