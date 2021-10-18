#!/usr/bin/env python3

import logging
from .base import get

logger = logging.getLogger(__name__)


def get_tests(use_v1_uptime_endpoints, apikey, username, tags=""):
    if use_v1_uptime_endpoints:
        page = 1
        endpoint = "uptime"
        params = {
            "tags": tags,
            "page": page
        }
        response = get(use_v1_uptime_endpoints, apikey, username, endpoint, params)
        tests = response.json()['data']
        while (page < (response.json()['metadata']['page_count'])):
            page += 1
            params["page"] = page
            response = get(use_v1_uptime_endpoints, apikey, username, endpoint, params)
            tests += response.json()['data']
    else:
        endpoint = "Tests"
        params = {
            "tags": tags
        }
        response = get(use_v1_uptime_endpoints, apikey, username, endpoint, params)
        tests = response.json()['data']

    return tests


def get_test_details(use_v1_uptime_endpoints, apikey, username, test_id):
    if use_v1_uptime_endpoints:
        endpoint = "uptime/%s" % test_id
        params = {}
    else:
        endpoint = "Tests/Details/"
        params = {
            "TestID": test_id
        }

    response = get(use_v1_uptime_endpoints, apikey, username, endpoint, params)

    return response
