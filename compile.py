#!/usr/bin/env python
import subprocess
import sys

def move(f):
    subprocess.call("mv %s output/" % f, shell=True)

def redirect_ouput_files(f):
    stem = f.split('.')[0]
    move(stem + ".aux")
    move(stem + ".log")
    move(stem + ".nav")
    move(stem + ".out")
    move(stem + ".pdf")
    move(stem + ".snm")
    move(stem + ".toc")

def open_slides(f):
    stem = f.split('.')[0]
    pdf_file = stem + ".pdf"
    subprocess.call("open output/%s" % pdf_file, shell=True)
    


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please specify a latex file."
    else:
        mylatex = sys.argv[1]
        subprocess.call("mkdir -p output", shell=True)
        subprocess.call("pdflatex %s" % mylatex, shell=True)
        redirect_ouput_files(mylatex)
        open_slides(mylatex)
