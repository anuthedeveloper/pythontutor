import sys
import getopt

# py main.py -m "Hello Python" -f "test.py" either ways

filename = "test.txt"
message = "Hello Python Tutorial"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)