#!/usr/bin/env python
#import python.template_collector as tc
import template_collector as tc

template = tc.template_AN
template = tc.template_2016
template = tc.template_plots
mykeys = tc.mykeys_three_years

template = tc.template_plots_year
mykeys = tc.mykeys_kinematics

def make_a_slide(slide):
    with open ("slides/" + slide["tex"], 'w') as f:
        #f.write( template.format(TITLE=slide["title"], FILE=slide["filename"]) )
        #f.write( template.format(TITLE=slide["title"], YEAR=2017, FILE=slide["filename"]) )
        f.write( template.format(TITLE=slide["title"], YEAR=2018, FILE=slide["filename"]) )

def make_slides():
    counter = 1
    fout = open("slides/content.tex", 'w')
    for title in mykeys:
        slide = {}
        slide["tex"] = "slide0%d.tex" % counter if counter<10 else "slide%d.tex" % counter
        slide["title"] = title
        slide["filename"] = tc.figures[title]
        make_a_slide(slide)
        fout.write("\input{slides/%s}\n" % slide["tex"])
        counter = counter + 1
    fout.close()

if __name__ == "__main__":
    make_slides()
