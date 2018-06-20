#chenqumi@20180518
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,re

if len(sys.argv) ==1:
    print("\nUsage: {} <>".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]

sam = []
with open(file) as fd:
    for line in fd:
                sam = line.strip().split("\t")
for instance in sam:
        print("{0}".format(instance))