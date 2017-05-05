# file for testing functionality
from collector.modules.github.repository import RepositoryService
from collector.modules.hh.builder import ParserBuilder
from collector.modules.hh.parser import Parser

parser_builder = ParserBuilder().set_region('2734')
parser = Parser(parser_builder)
parser.run()


# repository_service = RepositoryService('hughsk', 'uglifyify')
# repository_service.fetch_issues()

