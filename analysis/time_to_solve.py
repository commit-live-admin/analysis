import ast
from datetime import datetime


def get_execution_time(filepath):
    tree = ast.parse(''.join(open(filepath)))
    old_time = datetime.now()
    exec(compile(tree, filename="<ast>", mode="exec"))
    new_time = datetime.now()

    delta = new_time - old_time
    return delta.total_seconds()