import os
import re
import sys

prefix = input("Enter the target prefix:\n")
min_name_len = input("Enter mininal file name length:\n")
max_name_len = input("Enter maximal file name length:\n")
dir_list = os.listdir(".")
files_to_delete_count = 0

if len(prefix) > int(max_name_len):
    sys.exit("ERROR: The prefix if bigger than acceptable file name length")
for _file in dir_list:
    match = re.fullmatch("{pr}.{{{mn},{mx}}}".format(pr = prefix, mn = int(min_name_len) - len(prefix), mx = int(max_name_len) - len(prefix)), _file)
    if match == None:
        continue
    os.remove(match.group())
    files_to_delete_count += 1
print("Deleted " + str(files_to_delete_count) + " files.\n")
