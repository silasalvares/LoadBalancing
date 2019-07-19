import hashlib
from datetime import datetime
from enum import Enum

class StateEnum(Enum):
    CREATED = 'C'
    RUNNING = 'R'

def generate_id():
    hash = hashlib.sha1()
    hash.update(str(datetime.now()).encode('utf-8'))

    return str(hash.hexdigest()[:10])
