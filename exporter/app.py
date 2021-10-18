#!/usr/bin/env python3

import sys
import os
import time
import logging

from prometheus_client import start_http_server, REGISTRY
from collectors import test_collector
from utilities import logs, arguments
from setuptools import distutils


if __name__ == "__main__":

    try:

        args = arguments.get_args()

        logs.configure_logging(args.log_level)
        logger = logging.getLogger(__name__)

        logger.info("Starting web server")
        start_http_server(8000)

        logger.info("Registering collectors")
        REGISTRY.register(test_collector.TestCollector(
            bool(distutils.util.strtobool(args.use_v1_uptime_endpoints)), bool(distutils.util.strtobool(args.use_v1_maintenance_windows_endpoints)), args.username, args.api_key, args.tags))

        while True:
            time.sleep(1)

        sys.stdout.flush()

    except BrokenPipeError:

        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)
