from collector.router import Collector_Router
import numpy as np
import json


# params = {
#     'region': '2734'
# }


def create_collector_message(p):
    return {
        'module': 'hh',
        'params': p
    }


def average_salary(data):
    return int(np.mean(np.array(data)))


def max_salary(data):
    return int(np.max(data))


def min_salary(data):
    return int(np.min(data))


def create_result_by_function(params, data):
    if params['function'] == 'average':
        return average_salary(data)
    elif params['function'] == "min":
        return min_salary(data)
    elif params['function'] == "max":
        return max_salary(data)


def do_job(params):
    collector_message = create_collector_message(params)
    data_str = Collector_Router().set_message(collector_message).rpc()
    data = json.loads(data_str)
    data = list(map(int, data))
    # print(data)
    return create_result_by_function(params, data)



