#chenqumi@20180518
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,re

if len(sys.argv) ==1:
    print("\nUsage: {} <>".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]

sample = []
with open(file) as fd:
    for line in fd:
        sample = line.strip().split("\t")

for i in sample:
    print("{0}".format(i))

