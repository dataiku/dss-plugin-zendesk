import dataikuapi
import subprocess
import json
import os

client = dataikuapi.DSSClient(os.getenv('HOST'), os.getenv('API_KEY'))


def get_plugin_info():
    with open('plugin.json') as json_file:
        data = json.load(json_file)
        return data


def setup_module(module):
    result = subprocess.run(['make', 'plugin'], stdout=subprocess.PIPE)
    result.stdout
    info = get_plugin_info()
    with open('dist/dss-plugin-' + info["id"] + '-' + info["version"] + '.zip', 'rb') as file:
        client.get_plugin(get_plugin_info()["id"]).update_from_zip(file)


def scenario(project_key, scenario_id):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            client.get_project(project_key).get_scenario(scenario_id).run_and_wait()
            function(*args, **kwargs)
        return wrapper
    return real_decorator



