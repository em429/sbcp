#! python3

import os
import re
import sys
import shutil

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print('''Scans a folder for files with a certain extension and copies matches to target folder.
Usage: sbcp extension scan_folder target_folder''')
    sys.exit()

extension = sys.argv[1]
extension_regex = re.compile(r'.' + extension + '$')

scan_folder = sys.argv[2]
target_folder = sys.argv[3]


if not re.search('\/$', target_folder):
    print('Target folder name must end with a forward slash.')
    sys.exit()

for foldername, subfolders, filenames in os.walk(scan_folder):
    for filename in filenames:
        if extension_regex.search(filename):
            print(os.path.join(foldername, filename))
            shutil.copy(os.path.join(foldername, filename), target_folder + filename)
