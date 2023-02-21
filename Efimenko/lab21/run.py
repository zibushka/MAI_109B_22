import os


def checkSuffix(suffix, file):
    fileCopy = file
    fileCopy = fileCopy.split('.')
    fileCopy = fileCopy[0]
    fileCopy = fileCopy[len(fileCopy) - len(suffix):len(fileCopy)]
    return fileCopy == suffix


suffix = input("Enter suffix: ")
outFile = input(
    "Enter absolute path for output file or file name, if you want to create a file in the current directory: ")

outFile = os.path.abspath(outFile)
fileSize = 0
fileList = os.listdir()
blockSize = 2


if os.path.exists(outFile):
    os.remove(outFile)


for file in fileList:
    file = os.path.abspath(file)
    if os.path.isfile(file):

        if os.access(file, os.X_OK):
            print(f'{file} is executable!')

        else:
            if checkSuffix(suffix, file):
                fileSize = os.stat(file).st_size

                if fileSize % blockSize == 0:
                    os.system(f'echo {file} {fileSize} | tee -a {outFile}')
