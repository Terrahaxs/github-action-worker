import os
import json
from terrahaxs_worker.worker import worker, Payload

def run():
    payload = json.loads(os.getenv('PAYLOAD'))
    signature = os.getenv('SIGNATURE')
    worker(Payload(payload=payload), signature)

if __name__ == '__main__':
    run()