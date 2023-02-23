import argparse
import datetime
import os


def checkSuffix(suffix, file):
    fileCopy = file
    fileCopy = fileCopy.split('.')
    fileCopy = fileCopy[0]

    cutBegin = len(fileCopy) - len(suffix)
    cutEnd = len(fileCopy)

    fileCopy = fileCopy[cutBegin : cutEnd]

    return fileCopy == suffix


def writeData(suffix, outFile):
    outFile = os.path.abspath(outFile)
    fileList = os.listdir()
    blockSize = 2
    fileOut = open(outFile, 'w')

    for file in fileList:
        file = os.path.abspath(file)
        if os.path.isfile(file):

            if os.access(file, os.X_OK) == False:

                if checkSuffix(suffix, file):
                    fileSize = os.stat(file).st_size

                    if fileSize % blockSize == 0:
                        fileOut.write(f'echo {file} {fileSize}\n')


def main():
    now = datetime.datetime.now()
    nowTime = now.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("-sf", "--suffix", type=str, help='End of file name', required=True)
    parser.add_argument("-o", "--outFile", type=str, help='Path to output file', default=f'{nowTime}.txt')

    args = parser.parse_args()

    suffix = args.suffix
    outFile = args.outFile

    writeData(suffix, outFile)


if __name__ == "__main__":
    main()
