# Define the 'secret' command that allows you to use 'gpg' tool comfortably, securely.

from sys import argv, exit
from subprocess import call
import os
import filecmp

if len(argv) != 2:
    print('Usage: secret <filename>')
    exit(0)

# Note: filename = basename + extension
filename = argv[1]
basename, extension = os.path.splitext(filename)

if extension == ".gpg":
    call(["gpg", "-o", basename+".0", "-d", filename])
    call(["gpg", "-o", basename, "-d", filename])
    call(["subl", "-w", basename])
    
    if not filecmp.cmp(basename, basename+".0"):
        call(["rm", filename])
        call(["gpg", "--recipient", "Michael", "--encrypt", basename])
    
    call(["rm", basename])
    call(["rm", basename+".0"])      
else:
    call(["touch", filename])
    call(["subl", "-w", filename])
    call(["gpg", "--recipient", "Michael", "--encrypt", filename])
    call(["rm", filename])
