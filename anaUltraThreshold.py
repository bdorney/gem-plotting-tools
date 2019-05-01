#!/bin/env python

"""
anaUltraThreshold
=================
"""

if __name__ == '__main__':
    import argparse
    from gempython.gemplotting.utils.anaoptions import parent_parser
    parser = argparse.ArgumentParser(description="Options to give to anaUltraThreshold.py", parents=[parent_parser])
    parser.add_argument("--fileScurveFitTree", type=str, default=None, help="TFile containing scurveFitTree from this detector, if provided this will provide an updated chConfig file taking into account analysis here and data stored in the scurveFitTree")
    parser.add_argument("--isVFAT2", action="store_true", default=False, help="Provide this argument if input data was acquired from vfat2")
    parser.add_argument("--pervfat", action="store_true", help="Analysis for a per-VFAT scan (default is per-channel)")
    parser.add_argument("--doNotSavePlots", action="store_true", help="If provided output plots will not be made")
    parser.add_argument("--zscore", type=float, default=3.5, help="Z-Score for Outlier Identification in MAD Algo")

    from gempython.gemplotting.utils.anautilities import anaUltraThreshold
    parser.set_defaults(outfilename="ThresholdPlots.root",func=anaUltraThreshold)
    args = parser.parse_args()
   
    # Make output directory
    from gempython.utils.wrappers import runCommand
    filename = args.infilename[:-5]
    runCommand(["mkdir", "-p", "{0}".format(filename)])
    runCommand(["chmod", "g+rw", "{0}".format(filename)])

    # Run Analysis
    import ROOT as r
    inFile = r.TFile(filename+'.root')
    try:
        args.func(args,inFile.thrTree,filename)
    except RuntimeError as err:
        from gempython.utils.gemlogger import printRed
        printRed(err.message)
        inFile.Close()
        import os
        exit(os.EX_SOFTWARE)

    inFile.Close()
    print('Analysis Completed Successfully')
