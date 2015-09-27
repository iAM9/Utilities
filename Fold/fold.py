#! /usr/bin/python2 -OOt

import sys
import os
import shutil

command = sys.argv[0]
directoryName = sys.argv[1]
fileName = sys.argv[2]
filePath = sys.argv[3]

print 'here'

try:
	print "Running " + command


	newDirName = str(fileName) + " new"
	newDirPath = directoryName + "/" + newDirName

	os.mkdir(newDirPath)

	print newDirPath 
	print newDirName
	print fileName
	print filePath


	shutil.move(filePath, newDirPath)

except Exception, e:
	raise e


