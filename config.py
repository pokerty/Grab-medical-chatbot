import http.client
import logging
import os


def setup_examples():
    """
    Setup environment to easily run examples.
    API credentials need to be provided here in order
    to set up api object correctly.
    """
    try:
        import infermedica_api
    except ImportError:
        import sys

        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
        import infermedica_api

    # !!! SET YOUR CREDENTIALS AS ENVIRONMENTAL VARIABLES "APP_ID" & "APP_KEY" OR SET THEM HERE !!!
    app_id = os.getenv("APP_ID", "7c683f61")
    app_key = os.getenv("APP_KEY", "26cf180dd690889a9eb3cafbd6ddec36")

    # Prepare API v3 connector as default one
    infermedica_api.configure(
        **{
            "app_id": app_id,
            "app_key": app_key,
            "dev_mode": True,  # Use only during development or testing/staging, on production remove this parameter
        }
    )

    # Prepare API v2 connector under 'v2' alias
    infermedica_api.configure(
        **{
            "alias": "v2",
            "api_connector": "ModelAPIv2Connector",
            "app_id": app_id,
            "app_key": app_key,
            "dev_mode": True,  # Use only during development or testing/staging, on production remove this parameter
        }
    )

    # enable logging of requests and responses
    http.client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


# def get_example_request_data():
#     return {
#         "sex": "male",
#         "age": 30,
#         "evidence": [
#             {"id": "s_1193", "choice_id": "present", "source": "initial"},
#             {"id": "s_488", "choice_id": "present"},
#             {"id": "s_418", "choice_id": "absent"},
#         ],
#     }
