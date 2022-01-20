#!/usr/bin/env python
import subprocess
import sys
import datetime
today = datetime.datetime.today()
datetime_tag = today.strftime("%Y%m%d")

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

def update_and_open_slides(f):
    stem = f.split('.')[0]
    pdf_file_ori = stem + ".pdf"
    pdf_file_mod = stem + "_" + datetime_tag + ".pdf"
    subprocess.call("mv output/%s output/%s" % (pdf_file_ori, pdf_file_mod), shell=True)
    subprocess.call("open output/%s" % pdf_file_mod, shell=True)
    


if __name__ == "__main__":
    if len(sys.argv) < 2:
        mylatex = "tprime_hadronic_update.tex"
    else:
        mylatex = sys.argv[1]

    subprocess.call("mkdir -p output", shell=True)
    subprocess.call("pdflatex %s" % mylatex, shell=True)
    redirect_ouput_files(mylatex)
    update_and_open_slides(mylatex)
    print(">>> %s is used for making slides. :)" % mylatex)
