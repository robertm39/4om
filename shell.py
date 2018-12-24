# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:34:16 2018

@author: rober
"""

import interpreter

intp = interpreter.Interpreter(top=True)

while True:
    line = input('LINE: ')
    print(intp.interpret(line))