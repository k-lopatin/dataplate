from collector.modules.hh.builder import ParserBuilder
from collector.modules.hh.parser import Parser
from core.app import get_app


def try_cache(parser_builder):
    params_str = str(parser_builder)
    result = get_app().cache('collector').get(params_str)
    # result = None
    if result is None:
        print('none')
        parser = Parser(parser_builder)
        result = parser.run()
        get_app().cache('collector').set(params_str, result)
    return result


def do_job(params):
    parser_builder = ParserBuilder()

    if 'language' in params:
        parser_builder.set_language(params['language'])
    if 'region' in params:
        parser_builder.set_region(params['region'])
    if 'years_experience' in params:
        parser_builder.set_years_experience(params['years_experience'])

    return try_cache(parser_builder)
