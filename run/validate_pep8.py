from pylint import epylint as lint


def validate(filepath):
    (pylint_stdout, pylint_stderr) = lint.py_run(filepath, return_std=True)
    body = pylint_stdout.getvalue()
    return body
