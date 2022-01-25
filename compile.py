#!/usr/bin/env python
import subprocess
import sys
import datetime
today = datetime.datetime.today()
datetime_tag = today.strftime("%Y%m%d")

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', help='make slides', type=str, default="tex/tprime_hadronic_update.tex")
parser.add_argument('-m', help='make slides', action='store_true')
parser.add_argument('-e', help='compile tex file', action='store_true')
parser.add_argument('-t', help='tag of output files', type=str, default="")
args = parser.parse_args()

mytag = "AN"
mytag = "plots"
mytag = "2016"
mytag = args.t

#----------------------------------------------------------------------------------------------------

def move(f):
    subprocess.call("mv %s output/" % f, shell=True)

def redirect_ouput_files(f):
    move(stem + ".aux")
    move(stem + ".log")
    move(stem + ".nav")
    move(stem + ".out")
    move(stem + ".pdf")
    move(stem + ".snm")
    move(stem + ".toc")

def update_and_open_slides(f):
    pdf_file_ori = stem + ".pdf"
    pdf_file_mod = stem + "_" + mytag + "_" + datetime_tag + ".pdf"
    subprocess.call("mv output/%s output/%s" % (pdf_file_ori, pdf_file_mod), shell=True)
    subprocess.call("open output/%s" % pdf_file_mod, shell=True)
    
#----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    mylatex = args.i
    stem = mylatex.split('.')[0].split('/')[-1]
    print(">>> %s is used for making slides. :)" % mylatex)

    if args.m:
        subprocess.call("python ./python/slide_maker.py", shell=True)
        
    if args.e:
        subprocess.call("mkdir -p output", shell=True)
        subprocess.call("pdflatex %s" % mylatex, shell=True)
        redirect_ouput_files(mylatex)
        update_and_open_slides(mylatex)

    print(">>> finished!")
