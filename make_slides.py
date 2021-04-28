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
    \\item Background: ttH only
    \\end{{itemize}}
    \\end{{tiny}}

    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.2]{{mva12/THQHadronicTag_mytag_MVA_value_smh_varset8_{MYTAG}_{MVA}_n100_TprimeBToTH_M-{MASS}.png}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{column}}

%----------------------------------------------------------------------------------------------------
% 2nd column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.5\\textwidth}}
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.17]{{mva12/THQHadronicTag_mytag_accumulated_yields_MVA_value_smh_varset8_{MYTAG}_{MVA}_n100_TprimeBToTH_M-{MASS}.png}}}}\\qquad
        \\subfloat{{\\includegraphics[scale=0.17]{{mva12/THQHadronicTag_mytag_significance_MVA_value_smh_varset8_{MYTAG}_{MVA}_n100_TprimeBToTH_M-{MASS}.png}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{column}}

\\end{{columns}}
\\end{{frame}}
'''

def make_a_slide(filename, d):
    with open (filename, 'w') as f:
        f.write(template.format(TITLE=d["title"], MASS=d["mass"], RANGE=d["range"], MYTAG=d["mytag"], MVA=d["mva"]))

def make_slides():
    list_parameters = [
        {"filename":"slides/training_bdt_01.tex" , "title":"Training Result - TMVA BDT (1/10)"  , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva"},
        {"filename":"slides/training_bdt_02.tex" , "title":"Training Result - TMVA BDT (2/10)"  , "mass":625 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva"},
        {"filename":"slides/training_bdt_03.tex" , "title":"Training Result - TMVA BDT (3/10)"  , "mass":650 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva"},
        {"filename":"slides/training_bdt_04.tex" , "title":"Training Result - TMVA BDT (4/10)"  , "mass":675 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva"},
        {"filename":"slides/training_bdt_05.tex" , "title":"Training Result - TMVA BDT (5/10)"  , "mass":700 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva"},
        {"filename":"slides/training_bdt_06.tex" , "title":"Training Result - TMVA BDT (6/10)"  , "mass":800 , "range":"[800, 1000]" , "mytag":"mixed04", "mva":"tmva"},
        {"filename":"slides/training_bdt_07.tex" , "title":"Training Result - TMVA BDT (7/10)"  , "mass":900 , "range":"[800, 1000]" , "mytag":"mixed04", "mva":"tmva"},
        {"filename":"slides/training_bdt_08.tex" , "title":"Training Result - TMVA BDT (8/10)"  , "mass":1000, "range":"[800, 1000]" , "mytag":"mixed04", "mva":"tmva"},
        {"filename":"slides/training_bdt_09.tex" , "title":"Training Result - TMVA BDT (9/10)"  , "mass":1100, "range":"[1100, 1200]", "mytag":"mixed05", "mva":"tmva"},
        {"filename":"slides/training_bdt_10.tex" , "title":"Training Result - TMVA BDT (10/10)" , "mass":1200, "range":"[1100, 1200]", "mytag":"mixed05", "mva":"tmva"},
        {"filename":"slides/training_bdtg_01.tex", "title":"Training Result - TMVA BDTG (1/10)" , "mass":600 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_02.tex", "title":"Training Result - TMVA BDTG (2/10)" , "mass":625 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_03.tex", "title":"Training Result - TMVA BDTG (3/10)" , "mass":650 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_04.tex", "title":"Training Result - TMVA BDTG (4/10)" , "mass":675 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_05.tex", "title":"Training Result - TMVA BDTG (5/10)" , "mass":700 , "range":"[600, 700]"  , "mytag":"mixed03", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_06.tex", "title":"Training Result - TMVA BDTG (6/10)" , "mass":800 , "range":"[800, 1000]" , "mytag":"mixed04", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_07.tex", "title":"Training Result - TMVA BDTG (7/10)" , "mass":900 , "range":"[800, 1000]" , "mytag":"mixed04", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_08.tex", "title":"Training Result - TMVA BDTG (8/10)" , "mass":1000, "range":"[800, 1000]" , "mytag":"mixed04", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_09.tex", "title":"Training Result - TMVA BDTG (9/10)" , "mass":1100, "range":"[1100, 1200]", "mytag":"mixed05", "mva":"tmva_bdtg"},
        {"filename":"slides/training_bdtg_10.tex", "title":"Training Result - TMVA BDTG (10/10)", "mass":1200, "range":"[1100, 1200]", "mytag":"mixed05", "mva":"tmva_bdtg"},
    ]

    for d in list_parameters:
        make_a_slide(d["filename"], d)

if __name__ == "__main__":
    make_slides()
