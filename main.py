from collector.router import Collector_Router
from analytics.router import Analytics_Router
# file for testing functionality
from collector.modules.github.repository import RepositoryService
from collector.modules.hh.builder import ParserBuilder
from collector.modules.hh.parser import Parser


# parser_builder = ParserBuilder().set_region('2734')
# parser = Parser(parser_builder)
# parser.run()

def create_message(language):
    return {
        'module': 'hh',
        'params': {
            'region': '1',
            'language': language,
            'func': 'average'
        }
    }

languages = ['php', 'java', 'python', 'c#', 'javascript', 'go', 'android']

for language in languages:
    message = create_message(language)
    result = Analytics_Router().set_message(message).rpc()
    print(language)
    print(result)




# repository_service = RepositoryService('hughsk', 'uglifyify')
# repository_service.fetch_issues()
