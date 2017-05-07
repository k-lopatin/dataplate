import redis
import json
from core.modules.cache.base import BaseCache


class RedisCache(BaseCache):

    config_service = None

    def _init_config(self):
        self.host = self._get_param('host')
        self.port = self._get_param('port')
        self.db = self._get_param('db')
        self.r = self._get_connection()

    def _get_connection(self):
        return redis.StrictRedis(
            host=self.host,
            port=self.port,
            db=self.db
        )

    def _get_param(self, param):
        return self.config_service.get('core', 'cache', 'redis', param)

    def get(self, name):
        full_name = self._get_full_name(name)
        result = self.r.get(full_name)
        if result is not None:
            result = result.decode('utf-8')
        return result

    def set(self, name, value):
        full_name = self._get_full_name(name)
        if type(value) != str:
            value = json.dumps(value)
        self.r.set(full_name, value)