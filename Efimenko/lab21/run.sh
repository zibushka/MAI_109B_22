#!/bin/bash

echo "Enter suffix: "
read suffix
echo "Enter absolute path for output file or file name, if you want to create a file in the current directory: "
read outFile
path=$(pwd)

rm $outFile

for file in "$path"/*
do
    if [[ -f $file ]]
    then
        if [[ -x $file ]]
        then
            echo "$file is executable"
        else
            if [[ $file == *"$suffix."* ]]
            then
                size=$(ls -lh $file | cut -c30-36)
                echo "$file $size" | tee -a $outFile
            fi
        fi
    fi
done