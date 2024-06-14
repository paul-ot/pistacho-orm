import sqlite3
from contextlib import contextmanager

class Sqlite:
    def __init__(self, config):
        self._config = config
        self._connection = None

    def connect(self):
        if self._connection is None:
            self._connection = sqlite3.connect(self._config["path"])
        return self._connection

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    @contextmanager
    def database_connection(self):
        conn = self.connect()
        try:
            yield conn
        finally:
            pass
