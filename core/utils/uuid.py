from uuid import uuid4


def get_fresh_uuid():
    yield str(uuid4()).replace('-', '')
