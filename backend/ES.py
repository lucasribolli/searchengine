import yaml
from elasticsearch_dsl.connections import connections
from os.path import isfile

class ES:
    def __init__(self):
        file = '../common/config.yaml'
        if not isfile(file):
            file = './common/config.yaml'	
        with open(file) as f:
          config = yaml.load(f, Loader=yaml.FullLoader)
          host = config['elastic']['host']
          port = config['elastic']['port']

        connections.create_connection(host=host, port=port)