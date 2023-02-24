#!/bin/bash

echo "Enter the target prefix:"
read prefix
echo "Enter minimal file name length:"
read min_name_len
echo "Enter maximal file name length:"
read max_name_len

if [ ${#prefix} -gt $max_name_len ];
then
    echo "ERROR: The prefix is bigger than acceptable file name length";
    exit 1;
fi

files_to_delete_count=`find $prefix* |grep -x -E "[[:print:]]{$min_name_len,$max_name_len}" |wc -w`
find $prefix* | grep -x -E "[[:print:]]{$min_name_len,$max_name_len}" | xargs rm

echo "Deleted $files_to_delete_count files"
