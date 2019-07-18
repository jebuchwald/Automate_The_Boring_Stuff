#! python3
# bulkRename.py - Renames file names using regular expressions to find and replace patterns
# in this demo files named capitalsquiz<integer>.txt will be replaced with Capitals_Quiz_<integer>.txt
# refer to regex101.com for help creating regular expressions

import shutil, os, re

# Create a regex that matches what you want to replace
textPattern = re.compile(r"""^(.*?)
                         )
