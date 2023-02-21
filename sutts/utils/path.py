import os.path
import sys
from os import path

module_repo = [
    # "moegoe",
    "so_vits_svc"
]
project_root_path = \
    path.dirname(
        path.dirname(
            path.dirname(path.realpath(__file__))))
db_path = path.join(project_root_path, "db")

repositories_path = path.join(project_root_path, "repositories")

so_vits_svc_path = path.join(repositories_path, "so_vits_svc")
print("project_root_path", project_root_path)
print("repositories_path", repositories_path)


def add_dependencies():
    for module in module_repo:
        module_path = path.join(repositories_path, module)
        print("module", module, module_path)
        sys.path.append(module_path)
