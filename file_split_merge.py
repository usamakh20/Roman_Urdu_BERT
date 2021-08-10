import os
import sys
import argparse
from fsplit.filesplit import Filesplit

fs = Filesplit()

exclude_list_file = 'excluded_files'
manifest_file = 'fs_manifest.csv'
readme_file = 'README_IMPORTANT_DO_NOT_EDIT.txt'
current_script = os.path.basename(__file__)
readme_text = "File : {} is in split mode.\nPlease run at project root: " \
              "\"python3 {} --merge\" "

parser = argparse.ArgumentParser(
    epilog='To exclude files add the paths one per line in \"{}\".'.format(exclude_list_file))
parser.add_argument("--split", help="split all files within this directory greater than specified size",
                    action="store_true")
parser.add_argument("--merge", help="merge all files within this directory previously split by this program",
                    action="store_true")
parser.add_argument("--list", help="list all files that will be split given the specified size",
                    action="store_true")
parser.add_argument("--size", help="file size limit in bytes for splitting. Defaults to 100000000", type=int,
                    default=50000000)


def readable_size(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1000.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1000.0
    return "%.1f%s%s" % (num, 'Y', suffix)


def status(fname, s):
    print("file: {0}, size: {1}".format(fname, readable_size(s)))


def split(file_path: str, size: int = 100000000):
    output_path = file_path + '.parts'
    os.mkdir(output_path)
    fs.split(file=file_path, split_size=size, output_dir=output_path, callback=status)
    with open(output_path + '/' + readme_file, 'w') as file:
        file.write(readme_text.format(file_path, current_script))
    os.remove(file_path)


def merge(file_dir: str):
    file_path = '.'.join(file_dir.split('.')[:-1])
    fs.merge(input_dir=file_dir, output_file=file_path, callback=status, cleanup=True)
    os.remove(file_dir + '/' + readme_file)
    os.rmdir(file_dir)


def get_files_to_split(excluded_files, size: int = 100000000):
    result = []
    excluded_files = list(map(lambda x: os.path.join('.', x), excluded_files))
    for root, _, filenames in os.walk('.'):
        for file in filenames:
            file_path = os.path.join(root, file)
            if file_path not in excluded_files and os.stat(file_path).st_size > size and file != current_script:
                result.append(file_path)

    return result


def get_files_to_merge():
    result = []
    for root, _, _ in os.walk('.'):
        if root.split('.')[-1] == 'parts' and \
                os.path.isfile(os.path.join(root, manifest_file)) and \
                os.path.isfile(os.path.join(root, readme_file)):
            result.append(root)

    return result


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    files = []
    if os.path.isfile(exclude_list_file):
        with open(exclude_list_file, 'r') as f:
            files = f.read().strip().split('\n')
    else:
        with open(exclude_list_file, 'w'):
            pass

    # Read arguments from the command line
    args = parser.parse_args()
    if args.split:
        [split(file, args.size) for file in get_files_to_split(files, args.size)]

    elif args.merge:
        [merge(file) for file in get_files_to_merge()]

    elif args.list:
        [print(file) for file in get_files_to_split(files, args.size)]

# Todo:
# 1. enable adding folders to excluded files
# 2. add a check to so excluded_files itself is not split
# 3. Add feature to split or merge a single file
