import sys

command = sys.argv[1]
argument_len = len(sys.argv)
inputpath = sys.argv[2]
argument_02 = sys.argv[3]
contents = ''


def Validator(command, argument_len):
    if command == 'replace-string' and argument_len == 5:
        replaceString(inputpath, argument_02, sys.argv[4])
    elif command == 'reverse' and argument_len == 4:
        reverse(inputpath, argument_02)
    elif command == 'copy' and argument_len == 4:
        copy(inputpath, argument_02)
    elif command == 'duplicate-contents' and argument_len == 4:
        duplixateContents(inputpath, int(argument_02))
    else: 
        sys.stdout.buffer.write(b'The command or arguments are incorrect. \n')


def reverse(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
        contents = contents[::-1]
    with open(outputpath, 'w') as f:
        f.write(contents)

def copy(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)

def duplixateContents(inputpath, n):
    with open(inputpath) as f:
        contents = f.read()
    with open(inputpath, 'a') as f:
        for i in range(n):
            f.write('\n' + contents)

def replaceString(inputpath, needle, newstring):
    with open(inputpath) as f:
        contents = f.read()
        contents = contents.replace(needle, newstring)
    with open(inputpath, 'w') as f:
        f.write(contents)        


Validator(command, argument_len)