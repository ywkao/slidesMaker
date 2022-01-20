#!/usr/bin/env python

template = '''\\begin{{frame}}
\\frametitle{{ {TITLE} }}
\\begin{{columns}}
%----------------------------------------------------------------------------------------------------
% 1st column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.5\\textwidth}}
    \\begin{{tiny}}
    \\begin{{itemize}}
    \\item Signal sample: $M_{{T'}} = {MASS} GeV$
    \\item BDT trained with $M_{{T'}} \\in {RANGE} GeV$
    \\item Background: {CONTENT}
    {CONSTRAINT}
    \\end{{itemize}}
    \\end{{tiny}}

    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.2]{{slides/mva16/THQHadronicTag_mytag_MVA_value_{SAMPLE}_varset8_{MYTAG}_{MVA}_n100_TprimeBToTH_M-{MASS}.png}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{column}}

%----------------------------------------------------------------------------------------------------
% 2nd column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.5\\textwidth}}
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.17]{{slides/mva16/THQHadronicTag_mytag_accumulated_yields_MVA_value_{SAMPLE}_varset8_{MYTAG}_{MVA}_n100_TprimeBToTH_M-{MASS}.png}}}}\\qquad
        \\subfloat{{\\includegraphics[scale=0.17]{{slides/mva16/THQHadronicTag_mytag_significance_MVA_value_{SAMPLE}_varset8_{MYTAG}_{MVA}_n100_TprimeBToTH_M-{MASS}.png}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{column}}

\\end{{columns}}
\\end{{frame}}
'''

def make_a_slide(filename, d):
    with open ("slides/" + filename, 'w') as f:
        content = "non-resonant background" if d["sample"] == "nrb" else "only ttH"
        if d["sample"] == "nrb":
            constraint = ""
        if d["sample"] == "smh":
            value = 0.56 if d["mva"] == "tmva" else 0.94
            constraint = "\\item Cut value on BDT(NRB):  \\textcolor{red}{%s}" % str(value)
        f.write(template.format(TITLE=d["title"], MASS=d["mass"], SAMPLE=d["sample"], RANGE=d["range"], MYTAG=d["mytag"], MVA=d["mva"], CONTENT=content, CONSTRAINT=constraint))

def make_slides():
    list_parameters = [
        {"filename":"training_bdt_01.tex" , "title":"Training Result - BDT(NRB) (1/10)"  , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva"},
        #{"filename":"training_bdt_01.tex" , "title":"Training Result - BDT(NRB) (1/2)"   , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_02.tex" , "title":"Training Result - BDT(NRB) (2/10)"  , "mass":625 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_03.tex" , "title":"Training Result - BDT(NRB) (3/10)"  , "mass":650 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_04.tex" , "title":"Training Result - BDT(NRB) (4/10)"  , "mass":675 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_05.tex" , "title":"Training Result - BDT(NRB) (5/10)"  , "mass":700 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_06.tex" , "title":"Training Result - BDT(NRB) (6/10)"  , "mass":800 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_07.tex" , "title":"Training Result - BDT(NRB) (7/10)"  , "mass":900 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_08.tex" , "title":"Training Result - BDT(NRB) (8/10)"  , "mass":1000, "range":"[800, 1000]" , "mytag":"mixed04", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_09.tex" , "title":"Training Result - BDT(NRB) (9/10)"  , "mass":1100, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_10.tex" , "title":"Training Result - BDT(NRB) (10/10)" , "mass":1200, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"nrb", "mva":"tmva"},
        {"filename":"training_bdt_11.tex" , "title":"Training Result - BDT(SMH) (1/10)"  , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva"},
        #{"filename":"training_bdt_11.tex" , "title":"Training Result - BDT(SMH) (2/2)"   , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_12.tex" , "title":"Training Result - BDT(SMH) (2/10)"  , "mass":625 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_13.tex" , "title":"Training Result - BDT(SMH) (3/10)"  , "mass":650 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_14.tex" , "title":"Training Result - BDT(SMH) (4/10)"  , "mass":675 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_15.tex" , "title":"Training Result - BDT(SMH) (5/10)"  , "mass":700 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_16.tex" , "title":"Training Result - BDT(SMH) (6/10)"  , "mass":800 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_17.tex" , "title":"Training Result - BDT(SMH) (7/10)"  , "mass":900 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_18.tex" , "title":"Training Result - BDT(SMH) (8/10)"  , "mass":1000, "range":"[800, 1000]" , "mytag":"mixed04", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_19.tex" , "title":"Training Result - BDT(SMH) (9/10)"  , "mass":1100, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdt_20.tex" , "title":"Training Result - BDT(SMH) (10/10)" , "mass":1200, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"smh", "mva":"tmva"},
        {"filename":"training_bdtg_01.tex", "title":"Training Result - BDTG(NRB) (1/10)" , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva_bdtg"},
        #{"filename":"training_bdtg_01.tex", "title":"Training Result - BDTG(NRB) (1/2)"  , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_02.tex", "title":"Training Result - BDTG(NRB) (2/10)" , "mass":625 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_03.tex", "title":"Training Result - BDTG(NRB) (3/10)" , "mass":650 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_04.tex", "title":"Training Result - BDTG(NRB) (4/10)" , "mass":675 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_05.tex", "title":"Training Result - BDTG(NRB) (5/10)" , "mass":700 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_06.tex", "title":"Training Result - BDTG(NRB) (6/10)" , "mass":800 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_07.tex", "title":"Training Result - BDTG(NRB) (7/10)" , "mass":900 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_08.tex", "title":"Training Result - BDTG(NRB) (8/10)" , "mass":1000, "range":"[800, 1000]" , "mytag":"mixed04", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_09.tex", "title":"Training Result - BDTG(NRB) (9/10)" , "mass":1100, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_10.tex", "title":"Training Result - BDTG(NRB) (10/10)", "mass":1200, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"nrb", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_11.tex", "title":"Training Result - BDTG(SMH) (1/10)" , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva_bdtg"},
        #{"filename":"training_bdtg_11.tex", "title":"Training Result - BDTG(SMH) (2/2)"  , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_12.tex", "title":"Training Result - BDTG(SMH) (2/10)" , "mass":625 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_13.tex", "title":"Training Result - BDTG(SMH) (3/10)" , "mass":650 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_14.tex", "title":"Training Result - BDTG(SMH) (4/10)" , "mass":675 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_15.tex", "title":"Training Result - BDTG(SMH) (5/10)" , "mass":700 , "range":"[600, 700]"  , "mytag":"mixed03", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_16.tex", "title":"Training Result - BDTG(SMH) (6/10)" , "mass":800 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_17.tex", "title":"Training Result - BDTG(SMH) (7/10)" , "mass":900 , "range":"[800, 1000]" , "mytag":"mixed04", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_18.tex", "title":"Training Result - BDTG(SMH) (8/10)" , "mass":1000, "range":"[800, 1000]" , "mytag":"mixed04", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_19.tex", "title":"Training Result - BDTG(SMH) (9/10)" , "mass":1100, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"smh", "mva":"tmva_bdtg"},
        {"filename":"training_bdtg_20.tex", "title":"Training Result - BDTG(SMH) (10/10)", "mass":1200, "range":"[1100, 1200]", "mytag":"mixed05", "sample":"smh", "mva":"tmva_bdtg"},
    ]

    for d in list_parameters:
        make_a_slide(d["filename"], d)

if __name__ == "__main__":
    make_slides()
