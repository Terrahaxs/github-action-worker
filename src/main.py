import os
import json
from terrahaxs_runner.runner import runner
from terrahaxs_runner.models import Payload

def run():
    payload = json.loads(os.getenv('PAYLOAD'))
    signature = os.getenv('SIGNATURE')
    runner(Payload(payload=payload), signature)

if __name__ == '__main__':
    run()