import configparser
from elasticsearch_dsl.connections import connections


class ES:
    def __init__(self):
        config = configparser.ConfigParser()                                     
        config.read('./config.ini')

        HOST = config.get('ELASTIC', 'HOST')
        PORT = config.get('ELASTIC', 'PORT')

        connections.create_connection(host=HOST, port=PORT)