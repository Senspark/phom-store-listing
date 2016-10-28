#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v3.py metadata -platform iOS -prj-path . -sheet 1cFx92LErkPfHNbuljaWceJZdA6Kerg0gUcuJXN42ctc -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
