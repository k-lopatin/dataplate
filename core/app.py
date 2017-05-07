from config.service import ConfigService
from core.modules.cache.redis_cache.redis import RedisCache


class App:
    config = ConfigService()
    cache_for_component = {}

    def cache(self, component):
        RedisCache.config_service = self.config
        if component not in self.cache_for_component:
            self.cache_for_component[component] = RedisCache(component)
        return self.cache_for_component[component]


app = App()


def get_app():
    return app
