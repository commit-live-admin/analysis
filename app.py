#!/usr/bin/env python

from run.validate_pep8 import validate
from run.line_of_code import get_lines_of_code
from run.time_to_solve import get_execution_time
import requests
import sys

# file_path = "/Users/sangam/Documents/greyatom/analysis/run/module.py"
#
# print(validate(file_path))
# print(get_lines_of_code(file_path))
# print(get_execution_time(file_path))


def analyze(filepath, titleSlugTestCase, accessToken):
    pep8_warnings = validate(filepath)
    linenos = get_lines_of_code(filepath)
    executiontime = get_execution_time(filepath)

    url = "http://localhost:8080/v2/dumps/analysis"
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

    response = requests.post(url, json=params, headers=headers)


if __name__ == "__main__":
    filePath = sys.argv[1] # /Users/sangam/Documents/greyatom/analysis/run/module.py
    titleSlugTestCase = sys.argv[2] # fsdse-title-slug
    accessToken = sys.argv[3] # 60f126597ce4dccd7e716ed4ecf79c7b52a1d4c5
    analyze(filePath, titleSlugTestCase, accessToken)

