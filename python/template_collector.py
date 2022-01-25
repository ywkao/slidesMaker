#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------
# template
#----------------------------------------------------------------------------------------------------
template_2016 = '''\\begin{{frame}}
\\frametitle{{ {TITLE} }}
\\begin{{columns}}
%----------------------------------------------------------------------------------------------------
% 1st column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item EOY 2016
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison_20220120v3p6_std_2016/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}
%----------------------------------------------------------------------------------------------------
% 2nd column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item Reprocessed EOY 2016
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison_20220119v4p1_std_2016/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}

\\end{{columns}}
\\end{{frame}}
'''

template_plots_year = '''\\begin{{frame}}
\\frametitle{{ {TITLE} }}
\\begin{{columns}}
%----------------------------------------------------------------------------------------------------
% 1st column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item EOY
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison_20220120v3p6_std_{YEAR}/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}
%----------------------------------------------------------------------------------------------------
% 2nd column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item Ultra Legacy
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison_20220119v4p1_std_{YEAR}/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}

\\end{{columns}}
\\end{{frame}}
'''

template_plots = '''\\begin{{frame}}
\\frametitle{{ {TITLE} }}
\\begin{{columns}}
%----------------------------------------------------------------------------------------------------
% 1st column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item EOY
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison_20220120v3p6_std/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}
%----------------------------------------------------------------------------------------------------
% 2nd column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item Ultra Legacy
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison_20220119v4p1_std/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}

\\end{{columns}}
\\end{{frame}}
'''

template_AN = '''\\begin{{frame}}
\\frametitle{{ {TITLE} }}
\\begin{{columns}}
%----------------------------------------------------------------------------------------------------
% 1st column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item EOY
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{Data_MC_comparison/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}
%----------------------------------------------------------------------------------------------------
% 2nd column
%----------------------------------------------------------------------------------------------------
\\begin{{column}}{{0.60\\textwidth}}
\\begin{{itemize}}
    \\footnotesize
    \\item Ultra Legacy
    \\begin{{figure}}
        \\centering
        \\subfloat{{\\includegraphics[scale=0.25]{{ultraLegacy_samples/Data_MC_comparison/{FILE}}}}}
        \\label{{fig:mva_bdt}}
    \\end{{figure}}
\\end{{itemize}}
\\end{{column}}

\\end{{columns}}
\\end{{frame}}
'''

#ultraLegacy_samples
#Data_MC_comparison
#Data_MC_comparison_std_2016
#Data_MC_comparison_std_2017
#Data_MC_comparison_std_2018

# figures {{{
figures = {
    "Diphoton invariant mass" : "THQHadronicTag_Mass.pdf",
    "Mass\_sideband" : "THQHadronicTag_Mass_sideband.pdf",
    "Mass\_pass\_BDT\_smh\_cut\_mixed04" : "THQHadronicTag_Mass_pass_BDT_smh_cut_mixed04.pdf",
    "Mass\_pass\_BDT\_smh\_cut\_mixed03" : "THQHadronicTag_Mass_pass_BDT_smh_cut_mixed03.pdf",
    "Mass\_pass\_BDT\_smh\_cut\_mixed05" : "THQHadronicTag_Mass_pass_BDT_smh_cut_mixed05.pdf",
    "Tprime\_Mass\_pass\_BDT\_smh\_cut\_mixed03" : "THQHadronicTag_Tprime_Mass_pass_BDT_smh_cut_mixed03.pdf",
    "Tprime\_Mass\_pass\_BDT\_smh\_cut\_mixed05" : "THQHadronicTag_Tprime_Mass_pass_BDT_smh_cut_mixed05.pdf",
    "Tprime\_Mass\_pass\_BDT\_smh\_cut\_mixed04" : "THQHadronicTag_Tprime_Mass_pass_BDT_smh_cut_mixed04.pdf",
    "Mass\_tprime\_cov" : "THQHadronicTag_mass_tprime_cov.pdf",
    "PtHiggs" : "THQHadronicTag_PtHiggs.pdf",
    "Tprime\_pt\_ratio" : "THQHadronicTag_tprime_pt_ratio.pdf",
    "Helicity\_tprime" : "THQHadronicTag_helicity_tprime.pdf",
    "MetPt" : "THQHadronicTag_MetPt.pdf",
    "Mass\_top\_cov" : "THQHadronicTag_mass_top_cov.pdf",
    "Mass\_wboson\_cov" : "THQHadronicTag_mass_wboson_cov.pdf",
    "Mass\_tprime\_tilde" : "THQHadronicTag_mass_tprime_tilde.pdf",
    "Jet2BTag" : "Jet/THQHadronicTag_Jet2BTag.pdf",
    "Jet3Eta" : "Jet/THQHadronicTag_Jet3Eta.pdf",
    "Jet3BTag" : "Jet/THQHadronicTag_Jet3BTag.pdf",
    "Jet1Eta" : "Jet/THQHadronicTag_Jet1Eta.pdf",
    "Jet2\_ptOverM" : "Jet/THQHadronicTag_jet2_ptOverM.pdf",
    "Jet1\_ptOverM" : "Jet/THQHadronicTag_jet1_ptOverM.pdf",
    "Jet5Eta" : "Jet/THQHadronicTag_Jet5Eta.pdf",
    "Jet1BTag" : "Jet/THQHadronicTag_Jet1BTag.pdf",
    "Jet4\_ptOverM" : "Jet/THQHadronicTag_jet4_ptOverM.pdf",
    "Jet2Eta" : "Jet/THQHadronicTag_Jet2Eta.pdf",
    "Jet5BTag" : "Jet/THQHadronicTag_Jet5BTag.pdf",
    "Jet3\_ptOverM" : "Jet/THQHadronicTag_jet3_ptOverM.pdf",
    "Jet2pT" : "Jet/THQHadronicTag_Jet2pT.pdf",
    "Jet6pT" : "Jet/THQHadronicTag_Jet6pT.pdf",
    "Jet4pT" : "Jet/THQHadronicTag_Jet4pT.pdf",
    "Jet4BTag" : "Jet/THQHadronicTag_Jet4BTag.pdf",
    "Jet3pT" : "Jet/THQHadronicTag_Jet3pT.pdf",
    "Jet6BTag" : "Jet/THQHadronicTag_Jet6BTag.pdf",
    "Jet1pT" : "Jet/THQHadronicTag_Jet1pT.pdf",
    "Jet4Eta" : "Jet/THQHadronicTag_Jet4Eta.pdf",
    "Jet5pT" : "Jet/THQHadronicTag_Jet5pT.pdf",
    "Jet6Eta" : "Jet/THQHadronicTag_Jet6Eta.pdf",
    "Chi2\_wjet2\_eta" : "Chi2/THQHadronicTag_chi2_wjet2_eta.pdf",
    "Cov\_chi2\_value" : "Chi2/THQHadronicTag_cov_chi2_value.pdf",
    "Chi2\_tbw\_ptOverM" : "Chi2/THQHadronicTag_chi2_tbw_ptOverM.pdf",
    "Chi2\_wboson\_eta" : "Chi2/THQHadronicTag_chi2_wboson_eta.pdf",
    "Chi2\_tbw\_mass" : "Chi2/THQHadronicTag_chi2_tbw_mass.pdf",
    "Chi2\_wjet1\_ptOverM" : "Chi2/THQHadronicTag_chi2_wjet1_ptOverM.pdf",
    "Chi2\_wboson\_ptOverM" : "Chi2/THQHadronicTag_chi2_wboson_ptOverM.pdf",
    "Chi2\_wjet2\_ptOverM" : "Chi2/THQHadronicTag_chi2_wjet2_ptOverM.pdf",
    "Chi2\_wboson\_deltaR\_bjet" : "Chi2/THQHadronicTag_chi2_wboson_deltaR_bjet.pdf",
    "Chi2\_tbw\_deltaR\_dipho" : "Chi2/THQHadronicTag_chi2_tbw_deltaR_dipho.pdf",
    "Chi2\_wjet1\_pt" : "Chi2/THQHadronicTag_chi2_wjet1_pt.pdf",
    "Chi2\_bjet\_eta" : "Chi2/THQHadronicTag_chi2_bjet_eta.pdf",
    "Chi2\_tbw\_eta" : "Chi2/THQHadronicTag_chi2_tbw_eta.pdf",
    "Chi2\_wjet1\_eta" : "Chi2/THQHadronicTag_chi2_wjet1_eta.pdf",
    "Chi2\_wjets\_deltaR" : "Chi2/THQHadronicTag_chi2_wjets_deltaR.pdf",
    "Chi2\_bjet\_btagScores" : "Chi2/THQHadronicTag_chi2_bjet_btagScores.pdf",
    "Chi2\_wjet2\_btagScores" : "Chi2/THQHadronicTag_chi2_wjet2_btagScores.pdf",
    "Chi2\_wboson\_pt" : "Chi2/THQHadronicTag_chi2_wboson_pt.pdf",
    "Chi2\_tprime\_deltaR\_dipho" : "Chi2/THQHadronicTag_chi2_tprime_deltaR_dipho.pdf",
    "Chi2\_tprime\_ptOverM" : "Chi2/THQHadronicTag_chi2_tprime_ptOverM.pdf",
    "Chi2\_tbw\_pt" : "Chi2/THQHadronicTag_chi2_tbw_pt.pdf",
    "Chi2\_wjet2\_pt" : "Chi2/THQHadronicTag_chi2_wjet2_pt.pdf",
    "Chi2\_wjet1\_btagScores" : "Chi2/THQHadronicTag_chi2_wjet1_btagScores.pdf",
    "Chi2\_bjet\_ptOverM" : "Chi2/THQHadronicTag_chi2_bjet_ptOverM.pdf",
    "Chi2\_tprime\_eta" : "Chi2/THQHadronicTag_chi2_tprime_eta.pdf",
    "Chi2\_tprime\_deltaR\_tbw" : "Chi2/THQHadronicTag_chi2_tprime_deltaR_tbw.pdf",
    "Chi2\_bjet\_pt" : "Chi2/THQHadronicTag_chi2_bjet_pt.pdf",
    "Chi2\_wboson\_mass" : "Chi2/THQHadronicTag_chi2_wboson_mass.pdf",
    "MaxBTag" : "Had/THQHadronicTag_MaxBTag.pdf",
    "NbTight" : "Had/THQHadronicTag_NbTight.pdf",
    "NJets" : "Had/THQHadronicTag_NJets.pdf",
    "SecondMaxBTag" : "Had/THQHadronicTag_SecondMaxBTag.pdf",
    "HT" : "Had/THQHadronicTag_HT.pdf",
    "HT\_coarse" : "Had/THQHadronicTag_HT_coarse.pdf",
    "NbLoose" : "Had/THQHadronicTag_NbLoose.pdf",
    "NbMedium" : "Had/THQHadronicTag_NbMedium.pdf",
    "PhotonLeadIDMVA" : "Photon/THQHadronicTag_PhotonLeadIDMVA.pdf",
    "DiphotonCosPhi" : "Photon/THQHadronicTag_DiphotonCosPhi.pdf",
    "PhotonLeadPhi" : "Photon/THQHadronicTag_PhotonLeadPhi.pdf",
    "PhotonMaxIDMVA" : "Photon/THQHadronicTag_PhotonMaxIDMVA.pdf",
    "AbsCosHelicity" : "Photon/THQHadronicTag_AbsCosHelicity.pdf",
    "PhotonMaxIDMVA\_fine" : "Photon/THQHadronicTag_PhotonMaxIDMVA_fine.pdf",
    "PhotonSubleadPhi" : "Photon/THQHadronicTag_PhotonSubleadPhi.pdf",
    "PhotonSubleadPt" : "Photon/THQHadronicTag_PhotonSubleadPt.pdf",
    "PhotonSubleadPToM" : "Photon/THQHadronicTag_PhotonSubleadPToM.pdf",
    "PhotonLeadPToM" : "Photon/THQHadronicTag_PhotonLeadPToM.pdf",
    "PhotonMinIDMVA\_fine" : "Photon/THQHadronicTag_PhotonMinIDMVA_fine.pdf",
    "PhotonMinIDMVA" : "Photon/THQHadronicTag_PhotonMinIDMVA.pdf",
    "Rapidity" : "Photon/THQHadronicTag_Rapidity.pdf",
    "DiphotonPtOverMass" : "Photon/THQHadronicTag_DiphotonPtOverMass.pdf",
    "PhotonLeadEta" : "Photon/THQHadronicTag_PhotonLeadEta.pdf",
    "PhotonLeadPt" : "Photon/THQHadronicTag_PhotonLeadPt.pdf",
    "PhotonDeltaR" : "Photon/THQHadronicTag_PhotonDeltaR.pdf",
    "PhotonLeadPixelSeed" : "Photon/THQHadronicTag_PhotonLeadPixelSeed.pdf",
    "PhotonSubleadIDMVA" : "Photon/THQHadronicTag_PhotonSubleadIDMVA.pdf",
    "PhotonSubleadEta" : "Photon/THQHadronicTag_PhotonSubleadEta.pdf",
    "PhotonSubleadPixelSeed" : "Photon/THQHadronicTag_PhotonSubleadPixelSeed.pdf",

    "Mygraph_efficiency_MVA_value_nrb_varset8_mixed04_tmva_bdtg_n2000_TprimeBToTH_M-800_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_nrb_varset8_mixed04_tmva_bdtg_n2000_TprimeBToTH_M-800_linear.pdf",
    "Mytag_MVA_value_smh_varset8_mixed05_tmva_bdtg_n100_TprimeBToTH_M-1100" : "bdtg/THQHadronicTag_mytag_MVA_value_smh_varset8_mixed05_tmva_bdtg_n100_TprimeBToTH_M-1100.pdf",
    "Mygraph_efficiency_MVA_value_smh_varset8_mixed03_tmva_bdtg_n2000_TprimeBToTH_M-600_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_smh_varset8_mixed03_tmva_bdtg_n2000_TprimeBToTH_M-600_linear.pdf",
    "Mytag_MVA_value_smh_varset8_mixed03_tmva_bdtg_n100_TprimeBToTH_M-600" : "bdtg/THQHadronicTag_mytag_MVA_value_smh_varset8_mixed03_tmva_bdtg_n100_TprimeBToTH_M-600.pdf",
    "Mytag_MVA_value_smh_varset8_mixed05_tmva_bdtg_withNRBcut_n100_TprimeBToTH_M-1100" : "bdtg/THQHadronicTag_mytag_MVA_value_smh_varset8_mixed05_tmva_bdtg_withNRBcut_n100_TprimeBToTH_M-1100.pdf",
    "Mytag_MVA_value_nrb_varset8_mixed04_tmva_bdtg_n100_TprimeBToTH_M-800" : "bdtg/THQHadronicTag_mytag_MVA_value_nrb_varset8_mixed04_tmva_bdtg_n100_TprimeBToTH_M-800.pdf",
    "Mytag_MVA_value_smh_varset8_mixed03_tmva_bdtg_withNRBcut_n100_TprimeBToTH_M-600" : "bdtg/THQHadronicTag_mytag_MVA_value_smh_varset8_mixed03_tmva_bdtg_withNRBcut_n100_TprimeBToTH_M-600.pdf",
    "Mygraph_efficiency_MVA_value_nrb_varset8_mixed05_tmva_bdtg_n2000_TprimeBToTH_M-1100_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_nrb_varset8_mixed05_tmva_bdtg_n2000_TprimeBToTH_M-1100_linear.pdf",
    "Mygraph_efficiency_MVA_value_smh_varset8_mixed05_tmva_bdtg_n2000_TprimeBToTH_M-1100_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_smh_varset8_mixed05_tmva_bdtg_n2000_TprimeBToTH_M-1100_linear.pdf",
    "Mytag_MVA_value_nrb_varset8_mixed05_tmva_bdtg_n100_TprimeBToTH_M-1100" : "bdtg/THQHadronicTag_mytag_MVA_value_nrb_varset8_mixed05_tmva_bdtg_n100_TprimeBToTH_M-1100.pdf",
    "Mygraph_efficiency_MVA_value_smh_varset8_mixed04_tmva_bdtg_withNRBcut_n2000_TprimeBToTH_M-800_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_smh_varset8_mixed04_tmva_bdtg_withNRBcut_n2000_TprimeBToTH_M-800_linear.pdf",
    "Mygraph_efficiency_MVA_value_smh_varset8_mixed03_tmva_bdtg_withNRBcut_n2000_TprimeBToTH_M-600_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_smh_varset8_mixed03_tmva_bdtg_withNRBcut_n2000_TprimeBToTH_M-600_linear.pdf",
    "Mygraph_efficiency_MVA_value_smh_varset8_mixed05_tmva_bdtg_withNRBcut_n2000_TprimeBToTH_M-1100_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_smh_varset8_mixed05_tmva_bdtg_withNRBcut_n2000_TprimeBToTH_M-1100_linear.pdf",
    "Mytag_MVA_value_nrb_varset8_mixed03_tmva_bdtg_n100_TprimeBToTH_M-600" : "bdtg/THQHadronicTag_mytag_MVA_value_nrb_varset8_mixed03_tmva_bdtg_n100_TprimeBToTH_M-600.pdf",
    "Mytag_MVA_value_smh_varset8_mixed04_tmva_bdtg_n100_TprimeBToTH_M-800" : "bdtg/THQHadronicTag_mytag_MVA_value_smh_varset8_mixed04_tmva_bdtg_n100_TprimeBToTH_M-800.pdf",
    "Mytag_MVA_value_smh_varset8_mixed04_tmva_bdtg_withNRBcut_n100_TprimeBToTH_M-800" : "bdtg/THQHadronicTag_mytag_MVA_value_smh_varset8_mixed04_tmva_bdtg_withNRBcut_n100_TprimeBToTH_M-800.pdf",
    "Mygraph_efficiency_MVA_value_smh_varset8_mixed04_tmva_bdtg_n2000_TprimeBToTH_M-800_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_smh_varset8_mixed04_tmva_bdtg_n2000_TprimeBToTH_M-800_linear.pdf",
    "Mygraph_efficiency_MVA_value_nrb_varset8_mixed03_tmva_bdtg_n2000_TprimeBToTH_M-600_linear" : "bdtg/THQHadronicTag_mygraph_efficiency_MVA_value_nrb_varset8_mixed03_tmva_bdtg_n2000_TprimeBToTH_M-600_linear.pdf",

    "Jet2Phi" : "Jet/THQHadronicTag_Jet2Phi.pdf",
    "Jet4Phi" : "Jet/THQHadronicTag_Jet4Phi.pdf",
    "Jet3Phi" : "Jet/THQHadronicTag_Jet3Phi.pdf",
    "Jet1Phi" : "Jet/THQHadronicTag_Jet1Phi.pdf",
    "MetPhi" : "THQHadronicTag_MetPhi.pdf",
    "MetPt" : "THQHadronicTag_MetPt.pdf",
    "Chi2\_bjet\_phi" : "Chi2/THQHadronicTag_chi2_bjet_phi.pdf",
    "Chi2\_wjet1\_phi" : "Chi2/THQHadronicTag_chi2_wjet1_phi.pdf",
    "Chi2\_wjet2\_phi" : "Chi2/THQHadronicTag_chi2_wjet2_phi.pdf",
}
#}}}
# mykeys_three_years {{{
mykeys_three_years = [
    "Diphoton invariant mass",
    "Mass\_tprime\_cov",
    "Mass\_tprime\_tilde",
    "NJets",
    "NbLoose",
    "HT\_coarse",
    #"Mass\_wboson\_cov",
    #"Mass\_top\_cov",
    #"Mass\_sideband",
    #"Mass\_pass\_BDT\_smh\_cut\_mixed04",
    #"Mass\_pass\_BDT\_smh\_cut\_mixed03",
    #"Mass\_pass\_BDT\_smh\_cut\_mixed05",
    #"Tprime\_Mass\_pass\_BDT\_smh\_cut\_mixed03",
    #"Tprime\_Mass\_pass\_BDT\_smh\_cut\_mixed05",
    #"Tprime\_Mass\_pass\_BDT\_smh\_cut\_mixed04",
    "DiphotonPtOverMass",
    "PhotonMaxIDMVA\_fine",
    "PhotonMinIDMVA\_fine",
    "DiphotonCosPhi",
    "AbsCosHelicity",
    "Rapidity",
    "PhotonLeadPt",
    "PhotonLeadPToM",
    "PhotonLeadEta",
    "PhotonLeadPhi",
    "PhotonLeadPixelSeed",
    "PhotonLeadIDMVA",
    "PhotonSubleadPt",
    "PhotonSubleadPToM",
    "PhotonSubleadEta",
    "PhotonSubleadPhi",
    "PhotonSubleadPixelSeed",
    "PhotonSubleadIDMVA",
    "PhotonDeltaR",
    
    "MaxBTag",
    "SecondMaxBTag",
    "Jet1pT",
    "Jet2pT",
    "Jet3pT",
    "Jet4pT",
    "Jet1\_ptOverM",
    "Jet2\_ptOverM",
    "Jet3\_ptOverM",
    "Jet4\_ptOverM",
    "Jet1Eta",
    "Jet2Eta",
    "Jet3Eta",
    "Jet4Eta",
    "Jet1BTag",
    "Jet2BTag",
    "Jet3BTag",
    "Jet4BTag",
    "Chi2\_wjet1\_pt",
    "Chi2\_wjet1\_ptOverM",
    "Chi2\_wjet1\_eta",
    "Chi2\_wjet1\_btagScores",
    "Chi2\_wjet2\_pt",
    "Chi2\_wjet2\_ptOverM",
    "Chi2\_wjet2\_eta",
    "Chi2\_wjet2\_btagScores",
    "Chi2\_wjets\_deltaR",
    "Chi2\_bjet\_pt",
    "Chi2\_bjet\_ptOverM",
    "Chi2\_bjet\_eta",
    "Chi2\_bjet\_btagScores",
    "Chi2\_wboson\_pt",
    "Chi2\_wboson\_ptOverM",
    "Chi2\_wboson\_eta",
    "Chi2\_wboson\_mass",
    "Chi2\_wboson\_deltaR\_bjet",
    "Chi2\_tbw\_pt",
    "Chi2\_tbw\_ptOverM",
    "Chi2\_tbw\_eta",
    "Chi2\_tbw\_mass",
    "Chi2\_tbw\_deltaR\_dipho",
    "Cov\_chi2\_value",
    "Chi2\_tprime\_ptOverM",
    "Tprime\_pt\_ratio",
    "Chi2\_tprime\_eta",
    "Chi2\_tprime\_deltaR\_tbw",
    "Chi2\_tprime\_deltaR\_dipho",
    "Helicity\_tprime",
    "MetPt",
]
#}}}
# mykeys_kinematics {{{
mykeys_kinematics = [
    "Jet1pT",
    "Jet2pT",
    "Jet3pT",
    "Jet1Eta",
    "Jet2Eta",
    "Jet3Eta",
    "Jet1Phi",
    "Jet2Phi",
    "Jet3Phi",
    "Jet1BTag",
    "Jet2BTag",
    "Jet3BTag",
    "MetPt",
    "MetPhi",

    "Chi2\_wjet1\_pt",
    "Chi2\_wjet2\_pt",
    "Chi2\_bjet\_pt",
    "Chi2\_wjet1\_eta",
    "Chi2\_wjet2\_eta",
    "Chi2\_bjet\_eta",
    "Chi2\_wjet1\_phi",
    "Chi2\_wjet2\_phi",
    "Chi2\_bjet\_phi",
    "Chi2\_wjet1\_btagScores",
    "Chi2\_wjet2\_btagScores",
    "Chi2\_bjet\_btagScores",
]
#}}}
