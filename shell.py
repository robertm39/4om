# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:34:16 2018

@author: rober
"""

import interpreter
import om_4_runner

intp = interpreter.Interpreter(top=True)
#file = '4om_Test_Project\\main.4om'
file = '4om_Test_Project\\test.4om'
om_4_runner.run_file(file, intp)

while True:
    line = input('LINE: ')
    print(intp.interpret(line))

print('〈〉')