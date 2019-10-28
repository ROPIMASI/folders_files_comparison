"""
# CONTENT: PERSONAL MINI-PPROJECT.
# THEME: COMPARES WHETHER A LIST OF FOLDERS (OR FILES) IQUALS.
# PROJECT NAME: folders_files_comparison / ffc .
# FILE NAME: folders_files_comparison.py / ffc.
# PROJ-VERSION: 0.1.
# AUTHOR: RONALDO PI MA SI.
# DATE: 2019-JUN.
# LANGUAGE: PYTHON.
# LANG-VERSION: 3.
# PLATAFORM: Microsoft Windows7, PYTHON INTERPRETER 3.7.1, AND VISUAL STUDIO CODE.
# ---
# # IMPORTANT NOTE / DISCLAIMER:
# This is a project made exclusively for study purposes. Nobody has rights,
# obligations, either responsibility on it or its effects. There is no gua-
# rantee it will work correctly. It is not proprietary software, has no price,
# can not be sold.
# ---
# UNLICENSED:
# This is free and unencumbered software released into the public domain.
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# For more information, please refer to <http://unlicense.org>
"""



"""
SYNTAXES:
    ./ffc ...
"""



# coding: utf-8.
# Beginning with imports.
import os
import sys
# import time as t
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import webbrowser as wb



# ffc globals.
_acceptable_args_level_1 = ['?','sy','fo','fi','au','cs']



# MAIN FUNCTION.
def ffc(f1 , f2):
    # f1 and f2 mus be two folders path/name.
    print('folder 1=', f1)
    print('folder 2=', f2)
    return True



# Pre-processing:  recognizing the command line and its args.
if (sys.argv[0]=='./folders_files_comparison.py') or (sys.argv[0]=='./ffc'):
    # verify next step.
    if (len(sys.argv)==3): # v.0.0.1 beta compares 2 folders only.
        # Exists 2 args more. Must be 2 folders to be compared.
        ffc(sys.argv[1] , sys.argv[2])
    else
        # Error message: Does not exist only 2 args to be compared.
        print('\nError message: Does not exist only 2 args to be compared.')
else
    # Error message: Application file name has been modified.
    print('\nError message: Application file name has been modified.')


""" ### End. folders_files_comparison.py ends here. ### """
 
 
