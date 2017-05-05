import requests
from collector.modules.core.headers import get_headers


class AbstractParser(object):
    def get_page_by_link(self, link):
        return requests.get(link, headers=get_headers()).text
