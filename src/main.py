import os
from terrahaxs_worker.worker import worker, Payload

def run():
    token = os.getenv('TOKEN')
    worker(Payload(token=token))

if __name__ == '__main__':
    run()