import yaml
from elasticsearch_dsl.connections import connections


class ES:
    def __init__(self):
        with open('../common/config.yaml') as f:
          config = yaml.load(f, Loader=yaml.FullLoader)
          host = config['elastic']['host']
          port = config['elastic']['port']

        connections.create_connection(host=host, port=port)