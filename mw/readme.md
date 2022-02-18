run this cmd to generate a test_request.json dump
```
> python3 mw/collate_requests.py
```

The file contains all extractable requests from the yaml files against every path of portal server listed in app_vars.yml

Extractable requests are yaml/yml files with following structure:
```
requests:
 method: 'GET' / 'POST'
 path:
    - 'some/path'
```