r"""
``anaoptions`` --- Common options for analysis tools
====================================================

.. code-block:: python

    import gempython.gemplotting.utils.anahistory

Documentation
-------------
"""

#FIXME evetually remove the parser from OptionParser
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c","--channels", action="store_true", dest="channels",
                  help="Make plots vs channels instead of strips", metavar="channels")
parser.add_option("--chConfigKnown", action="store_true", dest="chConfigKnown",
                   help="Channel config already known", metavar="chConfigKnown")
parser.add_option("-d", "--debug", action="store_true", dest="debug",
                  help="print extra debugging information", metavar="debug")
parser.add_option("-i", "--infilename", type="string", dest="filename",
                  help="Specify Input Filename", metavar="filename")
parser.add_option("-p","--panasonic", action="store_true", dest="PanPin",
                  help="Make plots vs Panasonic pins instead of strips", metavar="PanPin")
parser.add_option("-o", "--outfilename", type="string", dest="outfilename",
                  help="Specify Output Filename", metavar="outfilename")
parser.add_option("--scandate", type="string", dest="scandate", default="current",
                  help="Specify specific date to analyze", metavar="scandate")
parser.add_option("--scandatetrim", type="string", dest="scandatetrim", default=None,
                  help="Specify the scan date of the trim run that corresponds to the chConfig.txt used in scandate", metavar="scandatetrim")
parser.add_option("-t", "--type", type="string", dest="GEBtype", default="long",
                  help="Specify GEB (long/short)", metavar="GEBtype")
parser.add_option("--ztrim", type="float", dest="ztrim", default=4.0,
                  help="Specify the p value of the trim", metavar="ztrim")

import argparse
parent_parser = argparse.ArgumentParser(add_help = False)

# Positional arguments
parent_parser.add_argument("infilename",type=str,help="Specify Input Filename by full path")
parent_parser.add_argument("GEBtype",type=str,help="Specify GEB type, options are 'long,short,m1,...,m8', if analyzing data from an ME0 detector write 'null'")

# Optional arguments
parent_parser.add_argument("-d", "--debug", action="store_true", help="print extra debugging information")
parent_parser.add_argument("-o", "--outfilename", type=str, help="Specify Output Filename")
parent_parser.add_argument("-t", "--type", type=str, dest="GEBtype", default="short", help="Specify GEB (long/short)")

stripChanOrPinType = parent_parser.add_mutually_exclusive_group(required=False)
stripChanOrPinType.add_argument("-c","--channels", action="store_true", help="Make plots vs channels instead of strips")
stripChanOrPinType.add_argument("-p","--panasonic", action="store_true", dest="PanPin",help="Make plots vs Panasonic pins instead of strips")
