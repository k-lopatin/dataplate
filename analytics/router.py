from core.router import BaseRouter
from analytics.modules.hh.main import do_job as hh_do_job


class Analytics_Router(BaseRouter):
    job = None

    def _do_rpc(self):
        if 'module' in self.message:
            self._choose_module()
        if 'params' in self.message:
            params = self.message['params']
        else:
            raise TypeError('params are not set')
        self.result = self.job(params)

    def _choose_module(self):
        if self.message['module'] == 'hh':
            self.job = hh_do_job