"""
Usage:
    versionman upgrade  PROJECT [--verbose] [--root-path=PATH]
    versionman downgrade PROJECT [--verbose] [--root-path=PATH]
    versionman --version
    version -h | --help

Options:
    -h --help           Show this screen
    --root-path=PATH    Root path for search context of projects [default: C:\dev_\git]
    --version           Shows the version of VersionMan
    --verbose           Executes the commands more textual
"""

from docopt import docopt
from os import listdir
from os.path import join
from maven import maven as mvn
from maven import versionutils

VERSIONMAN_VERSION = "VersionMan v0.0.1"


def log_function(func):
    """
    A decorator to log arguments of function
    """

    fname = func.__code__.co_name
    arg_names = func.__code__.co_varnames
    def echo_func(*args, **kwargs):
        """
        Echoes the function arguments
        """
        print("[!]", fname + ": ", ", ".join("%s=%r" % entry for entry in zip(arg_names, args)))
        return func(*args, **kwargs)
    return echo_func

@log_function
def upgrade(project_root_path):
    print("[!] mvn version upgrade operation is started")
    success, out = mvn.get_version(project_root_path)
    if success:
        current_version = out
        new_version = versionutils.increase_version_minor(current_version)
        print("[!] Current version of the project is", current_version)
        print("[!] Increased version of the project is", new_version)
        success, out = mvn.set_version(project_root_path, new_version)
        if success:
            print("[!] Version updated.")
        else:
            print(out)

@log_function
def downgrade(project_root_path):
    print("[!] mvn version downgrade operation is started")
    success, out = mvn.get_version(project_root_path)
    if success:
        current_version = out
        new_version = versionutils.decrease_version_minor(current_version)
        print("[!] Current version of the project is", current_version)
        print("[!] Downgraded version of the project is", new_version)
        success, out = mvn.set_version(project_root_path, new_version)
        if success:
            print("[!] Version updated.")
        else:
            print(out)

if __name__ == '__main__':
    ARGUMENTS = docopt(__doc__, version=VERSIONMAN_VERSION)
    ROOT_PATH = ARGUMENTS['--root-path']
    PROJECTS = [p for p in listdir(ROOT_PATH) if p == ARGUMENTS['PROJECT']]

    if len(PROJECTS) == 1:
        PROJECT_PATH = join(ROOT_PATH, PROJECTS[0])
        if ARGUMENTS['upgrade']:
            upgrade(PROJECT_PATH)
        elif ARGUMENTS['downgrade']:
            downgrade(PROJECT_PATH)
