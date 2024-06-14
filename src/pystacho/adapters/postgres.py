import psycopg2.pool
from contextlib import contextmanager


class Postgres:
    def __init__(self, config):
        self._config = config

    def connection_pool(self):
        return psycopg2.pool.SimpleConnectionPool(
            2,
            self._config["pool_size"],
            user=self._config["user"],
            password=self._config["password"],
            host=self._config["host"],
            port=self._config["port"],
            database=self._config["name"])

    @contextmanager
    def database_connection(self):
        connection = self.connection_pool().getconn()
        try:
            yield connection
        finally:
            connection.close()
