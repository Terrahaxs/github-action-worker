import os
import json
from terrahaxs_worker.worker import worker, Payload

def run():
    payload = json.loads(os.getenv('PAYLOAD'))
    print(payload)
    worker(Payload(payload=payload))

if __name__ == '__main__':
    run()