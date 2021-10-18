#!/usr/bin/env python3

import logging
import requests

STATUS_CAKE_BASE_URL = "https://app.statuscake.com/API/"
V1_STATUS_CAKE_BASE_URL = "https://api.statuscake.com/v1/"

logger = logging.getLogger(__name__)


def get(use_v1_api, apikey, username, endpoint, params={}):

    if use_v1_api:
        headers = {
            "Authorization": "Bearer %s" % apikey
        }
        BASE_URL = V1_STATUS_CAKE_BASE_URL
    else:
        headers = {
            "API": apikey,
            "Username": username
        }
        BASE_URL = STATUS_CAKE_BASE_URL

    request_url = "{base}{endpoint}".format(
        base=BASE_URL, endpoint=endpoint)

    logger.debug("Starting request: {request_url} {endpoint} {params}".format(
        request_url=request_url,
        endpoint=endpoint,
        params=params))

    response = requests.get(url=request_url, params=params, headers=headers)
    response.raise_for_status()

    return response
