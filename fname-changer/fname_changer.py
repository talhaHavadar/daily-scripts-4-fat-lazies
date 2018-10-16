"""fname_changer is python script that changes the file names in execution directory by given replacement strings.

Usage:
    fname_changer.py ROOT_PATH SEARCH REPLACEMENT [--file-extension=<ext>, --case-insensitive]
    fname_changer.py --version
    fname_changer.py --help
    fname_changer.py -h

Options:
    -h --help               Shows this screen
    --version               Shows version.
    --file-extension=<ext>  Filters the files by extension [default: *]
    --case-insensitive      Case insensitivity for comparing SEARCH string with file names.
"""
from docopt import docopt
import glob
import os

def get_files(path: str, extension: str) -> [str]:
    return glob.glob(os.path.join(".", path, "**", "*." + extension), recursive= True)

if __name__ == '__main__':
    arguments = docopt(__doc__, version="===fname_changer===\n   Version 1.0")
    IGNORE_CASE = arguments["--case-insensitive"]
    EXTENSION = arguments["--file-extension"] if not arguments["--file-extension"].startswith(".") else arguments["--file-extension"][1:]
    SEARCH = arguments["SEARCH"] if not IGNORE_CASE else arguments["SEARCH"].lower()
    REPLACEMENT = arguments["REPLACEMENT"]
    PATH = arguments["ROOT_PATH"]

    print("[*] Searching for the files..")
    files = get_files(PATH, EXTENSION)

    if files:
        print("[*] Files found.")
        for f in files:
            print("\t[-]", f)
        print("####################################################################################")
        modified = 0
        for f in files:
            f_name = os.path.basename(f) if not IGNORE_CASE else os.path.basename(f.lower())
            dir_name = os.path.dirname(f)
            if SEARCH in f_name:
                f_name = f_name.replace(SEARCH, REPLACEMENT)
                new_path = os.path.join(dir_name, f_name)
                os.rename(f, new_path)
                print("[!] Changed:", f, "=>", new_path)
                modified += 1
        print(f"[*] {modified} file{'s' if modified > 1 else ''} modified.")
    else:
        print("[*] No files found.")
