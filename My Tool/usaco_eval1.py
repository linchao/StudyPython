#! /usr/bin/env python3
# Filename: usaco_eval.py

import os
import time

prog = 'game1'
test_path = r'D:\成长\实习\挑战的快乐\USACO\USACO全部测试数据\3.3.5 A Game'

input_path = 'D:\\Project\\StudyPython\\My Tool\\' + prog + '.in'
exec_path = r'D:\成长\实习\挑战的快乐\USACO\usaco\Debug\usaco'

output_path = input_path.replace('.in', '.out')
testfiles = os.listdir(test_path)

isCorrect = True
testnum = 1
for filename in testfiles:
    if (filename.startswith('input')):

        # produce the test file
        testfile = open(test_path + os.sep + filename)
        inputfile = open(input_path, 'w')
        while True:
            line = testfile.readline()
            if len(line) == 0:
                break
            inputfile.write(line)
        inputfile.close()

        # executing the cmd
        os.system(exec_path)

        # check the answer
        checkname = filename.replace('input', 'output')
        checkfile = open(test_path + os.sep + checkname)
        ouputfile = open(output_path)

        while True:
            ol = ouputfile.readline()
            cl = checkfile.readline()
            if ol != cl:
                isCorrect = False
                break
            if len(ol) == 0:
                break

        if isCorrect == False:
            print ('Sorry, my darling.\n%s goes wrong.' % filename)
            break
        print ("test %d has been success." %testnum)
        testnum += 1
        ouputfile.close()
        checkfile.close()
if isCorrect:
    print ('Genius, you are right.')
        



