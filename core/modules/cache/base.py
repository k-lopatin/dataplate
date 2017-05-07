class BaseCache:
    global_prefix = 'dataplate'
    prefix = ''

    def __init__(self, component):
        self.component = component
        self._init_config()
        self._create_prefix()

    def _init_config(self):
        raise NotImplemented()

    def _create_prefix(self):
        self.prefix = "%s_%s" % (self.global_prefix, self.component)

    def set(self, name, value):
        raise NotImplemented()

    def get(self, name):
        raise NotImplemented

    def _get_full_name(self, name):
        return "%s_%s" % (self.prefix, name)
