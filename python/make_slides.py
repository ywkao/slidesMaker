#!/usr/bin/env python
#import python.template_collector as tc
import template_collector as tc

def make_a_slide(slide):
    with open ("slides/" + slide["tex"], 'w') as f:
        f.write( tc.template.format(TITLE=slide["title"], FILE=slide["filename"]) )

def make_slides():
    counter = 1
    for title in tc.mykeys:
        slide = {}
        slide["tex"] = "slide0%d.tex" % counter if counter<10 else "slide%d.tex" % counter
        slide["title"] = title
        slide["filename"] = tc.figures[title]
        make_a_slide(slide)
        counter = counter + 1

if __name__ == "__main__":
    make_slides()
