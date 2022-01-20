#!/usr/bin/env python

txt = "slides/tables.tex"
output = "slides/my_table_of_yields.csv"

def extract_info():
    with open(output, 'w') as fout:
        with open(txt, 'r') as fin:
            for line in fin.readlines():
                content = line.strip()
                if 'hM' in content:
                    print content
                if 'pm' in content:
                    print content

if __name__ == "__main__":
    extract_info()
