#!/usr/bin/env python3
#NB - all of these import statements should specify their versions and be executed in a separate script at Docker build time.
import os
import sys
from subprocess import call

WORKING_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
ROOT = os.path.join(WORKING_DIR, '..')
TASKLIB = os.path.join(ROOT, 'src/')
INPUT_FILE_DIRECTORIES = os.path.join(ROOT, 'data/')

command_line = "python "+TASKLIB+"LogNormalize.py"\
                + " -F " + INPUT_FILE_DIRECTORIES+"test.gct"\
                + " -o created_file_ground_truth"
print("About to call the module using the command line:", command_line)

call(command_line, shell=True)