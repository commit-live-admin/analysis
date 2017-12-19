#!/usr/bin/env python

from analysis.validate_pep8 import validate
from analysis.line_of_code import get_lines_of_code
from analysis.time_to_solve import get_execution_time
import requests
import json
import sys


def analyze(filepath, titleSlugTestCase, accessToken, env, hash):
    pep8_warnings = validate(filepath)
    linenos = get_lines_of_code(filepath)
    executiontime = get_execution_time(filepath)

    domain = "https://api2.commit.live"
    if(env == "dev"):
        domain = "http://api.greyatom.com"
    elif (env == "local"):
        domain = "http://localhost:8080"

    url = domain + "/v2/dumps/analysis"
    headers = {
        "Content-Type": "application/json",
        "Authorization":  accessToken
    }

    params = {
        'warninggs': pep8_warnings,
        'lines': linenos,
        'executionTime': executiontime,
        'titleSlugTestCase': titleSlugTestCase,
        'hash': hash
    }

    print json.dumps(params)
    # response = requests.post(url, json=params, headers=headers)

if __name__ == "__main__":
    # env = "prod"
    # accessToken = "60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5"
    # hash = "hash"
    # titleSlugTestCase = "fsdse-title-slug"
    # filePath =  "/Users/sangam/Documents/greyatom/analysis/analysis/module.py"

    env = sys.argv[1]
    accessToken = sys.argv[2]
    hash = sys.argv[3]
    titleSlugTestCase = sys.argv[4]
    filePath = sys.argv[5]
    analyze(filePath, titleSlugTestCase, accessToken, env, hash)
