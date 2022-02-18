import os
import yaml
import json

test_requests = []

def get_endpoints():
    with open('mw/app_vars.yml', "r") as stream:
        req_vars_yaml_data = yaml.safe_load(stream)
        return req_vars_yaml_data['endpoints']

def write_extracted_requests(req_yaml_data):
    try:
        if 'requests' in req_yaml_data.keys():
            for req in req_yaml_data['requests']:
                if 'path' in req.keys():
                    for path in req['path']:
                        extracted_req = {}
                        if path == '{{BaseURL}}':
                            continue
                        if 'method' in req.keys():
                            extracted_req['method'] = req['method']
                        if 'body' in req.keys():
                            extracted_req['body'] = req['body']
                        for endpoint in get_endpoints():
                            extracted_req['path'] = path.replace('{{BaseURL}}', endpoint)
                            test_requests.append(extracted_req.copy())
    except yaml.YAMLError as exc:
        print(exc)

def read_files():
    for root, dirs, files in os.walk('../kenzer-templates/'):
        if not root.endswith('mw'):
            for file in files:
                if file.endswith('yaml') or root.endswith('yml'):
                    with open(root + '/' + file, "r") as stream:
                        try:
                            write_extracted_requests(yaml.safe_load(stream))
                        except Exception as e:
                            print('error: {} \nfile: {} \n\n'.format(e, root + '/' + file))
                            continue

def dump_json():
    with open('mw/test_request.json', 'w') as yaml_file:
        json.dump(test_requests, yaml_file, ensure_ascii=False, indent=4)

read_files()
dump_json()
