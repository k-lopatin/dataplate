from configobj import ConfigObj


class ConfigService:

    def get(self, component, module, name, parameter):
        filename = _build_filename(component, module, name)
        config = ConfigObj(filename)
        return config[parameter]

    def set(self, component, module, name, parameters):
        filename = _build_filename(component, module, name)
        config = ConfigObj()
        config.filename = filename
        self.set_params(config, parameters)
        config.write()

    def set_params(self, config, parameters):
        for name, value in parameters.items():
            config[name] = value


def _build_filename(component, module, name):
    return component + '/modules/' + module + '/config/' + name + '.ini'
