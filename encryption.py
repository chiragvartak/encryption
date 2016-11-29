# Define the 'secret' command that allows you to use 'gpg' tool comfortably, securely.

from sys import argv
from subprocess import call
import os

# Note: filename = basename + extension
filename = argv[1]
basename, extension = os.path.splitext(filename)

file_exists = os.path.isfile(filename)

if extension == ".gpg":
    call(["gpg", "-o", basename, "-d", filename])
    call(["subl", "-w", basename])
    call(["rm", filename])
    call(["gpg", "--recipient", "Michael", "--encrypt", basename])
    call(["rm", basename])
else:
    call(["touch", filename])
    call(["subl", "-w", filename])
    call(["gpg", "--recipient", "Michael", "--encrypt", filename])
    call(["rm", filename])
