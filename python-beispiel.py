#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re

def main (argv):
    gedankenstriche_pattern = re.compile(r" - ")
    with open("Daten/Koalitionsvertrag.txt", "r") as input_file:
        text = input_file.read()
        
        print "gedankenstriche_pattern.search(text)"
        search_result = gedankenstriche_pattern.search(text)
        print search_result
        print "gedankenstriche_pattern.search.group(0)"
        print search_result.group(0)
        
        print "gedankenstriche_pattern.findall(text)"
        findall_result = gedankenstriche_pattern.findall(text)
        print findall_result
        
        print "gedankenstriche_pattern.sub(' -- ', text)"
        print gedankenstriche_pattern.sub(' -- ', text)
        

if __name__ == "__main__":
    main(sys.argv[1:])