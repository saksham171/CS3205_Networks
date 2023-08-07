Lab2-DNS.pdf:
    Problem Statement for the lab assignment.

lab2-cs20b067.py:
    The source file for running the heirarchial DNS system.

input.txt:
    The default input file for the source file.

typescript:
    The script file after running 'script' command and then running the source file.

COMMENTS.md:
    The comments file for my experience with the assignment.

Makefile:
    The makefile for the source file.

The source file is written in python3 and can be run using the following command (startPort > 1024):
python3 lab2-cs20b067.py startPort inputfile

To remove the generated log files, run the following command:
make clean

To run the source file with the default input file(input.txt) and default port number(10000), run the following command:
make
