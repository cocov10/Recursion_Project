import sys
import markdown

# python3 file-converter.py markdown sample.md index.html

command = sys.argv[1].lower()
inputfile = sys.argv[2]
outputfile = sys.argv[3]
argument_len = len(sys.argv)
contents = ''
html = ''

def Validator(command, argument_len):
    if command == 'markdown' and argument_len == 4:
        markdownHTML(inputfile, outputfile)
    else:
        sys.stdout.buffer.write(b'The command or arguments are incorrect. \n')

def markdownHTML(inputfile, outputfile):
    with open(inputfile, 'r', encoding='utf-8') as f:
        contents = f.read()
    html = markdown.markdown(contents)
    with open(outputfile, 'w', encoding='utf-8', errors='xmlcharrefreplace') as f:
        f.write(html)


Validator(command, argument_len)







