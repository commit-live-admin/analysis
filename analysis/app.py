#!/usr/bin/env python

from analysis.validate_pep8 import validate
from analysis.line_of_code import get_lines_of_code
from analysis.time_to_solve import get_execution_time
import requests
import json


def analyze(filepath, titleSlugTestCase, accessToken, env, dumpId):
    pep8_warnings = validate(filepath)
    linenos = get_lines_of_code(filepath)
    executiontime = get_execution_time(filepath)

    domain = "https://api2.commit.live"
    if(env == "dev"):
        domain = "http://api.greyatom.com"
    elif (env == "local"):
        domain = "http://localhost:8080"

    url = domain + "/v2/dumps/analysis/" + dumpId

    headers = {
        "Content-Type": "application/json",
        "Authorization":  accessToken
    }

    params = {
        'warninggs': pep8_warnings,
        'lines': linenos,
        'executionTime': executiontime,
        'titleSlugTestCase': titleSlugTestCase
    }

    requests.post(url, json=params, headers=headers)


