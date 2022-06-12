## Instructions

This git contains 2 versions of the chatbot, both using the infermedica api. One is a command line one with accurate responses. The other is a web app created with Flask with a beautiful interface.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask. Then upgrade it to version 2.0 and above.

```bash
pip install flask
pip install flask --upgrade
```

Request for a developer account at https://developer.infermedica.com for app_key and app_id and set it in config.py (line 21 and 22)


## Usage

```python
from flask import Flask, render_template, request, jsonify, redirect, url_for
```

```python
import infermedica_api
api: infermedica_api.APIv3Connector = infermedica_api.get_api()
```
To use the web chatbot, run app.py
```python
python app.py
```
To use the command line chatbot, run chat2.py
```python
python chat2.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
