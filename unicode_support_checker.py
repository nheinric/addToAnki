# See http://stackoverflow.com/questions/7030857/displaying-utf8-stings-in-ubuntus-terminal-with-a-python-script for unicode stuff
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
import re
import unicodedata

if not (("PYTHONIOENCODING" in os.environ) and re.search("^utf-?8$", os.environ["PYTHONIOENCODING"], re.I)):
    sys.stderr.write(sys.argv[0] + ": Please set your PYTHONIOENCODING envariable to utf8\n");
    sys.exit(1);

if unicodedata.unidata_version < "6.0.0":
    print("WARNING: Your old UCD is out of date, expected at least 6.0.0 but got "+unicodedata.unidata_version);

wide_enough = (sys.maxunicode >= 0x10FFFF);
if not wide_enough:
    print("WARNING: Narrow build detected, your Python lacks full Unicode support!!");

