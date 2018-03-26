import os
import sys
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
from shutil import copyfile

# Joseph Ly, Fall 2016
# Project 2 Bonus

# The file name 
FILE_NAME = "codearray.h";

###########################################################
# This part uses the windows Powershell to a hexadecimal dump
##########################################################
def getHexDump(execPath):
	
	print("Getting hexdump...")
	# Get the hexdump
	#subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "gc", execPath, "-Encoding Byte | % { ($_ | % { “{0:X2}” -f $_ }) | Out-File output.txt -Append -Encoding ASCII}"])
	
	subprocess.call(["powershell", "gc", execPath, "-Encoding Byte | % { ($_ | % { “{0:X2}” -f $_ }) | Out-File output.txt -Append -Encoding ASCII}"])
	
	copyfile("output.txt", "hex.txt")
	os.remove("output.txt")
	
	with open("hex.txt", "r") as r:
		retVal = []
		for line in r:
			retVal.append(line)
		
	uguu = [i.replace('\n', '') for i in retVal] # Remove \n from each element
	return uguu
	
###################################################################
# Generates the header file containing an array of executable codes
# @param execList - the list of executables
# @param fileName - the header file to which to write data
###################################################################

def generateHeaderFile(execList, fileName):

	# The header file
	headerFile = None

	# The program array
	progNames = sys.argv

	# Open the header file
	headerFile = open(fileName, "w")

	# The program index
	progCount = 0

	# The lengths of programs
	progLens = []

	# Write the array name to the header file
	headerFile.write("#include <string>\n\nusing namespace std;\n\nunsigned char* codeArray[] = {");
	
	last = execList[-1] # Grab the last element in the list

	# For each program progName we should run getHexDump() and get the 
	# the string of bytes formatted according to C++ conventions. That is, each
	# byte of the program will be a two-digit hexadecimal value prefixed with 0x. 
	# For example, 0xab. Each such byte should be added to the array codeArray in 
	# the C++ header file. 
	for progName in execList:
		bomb = getHexDump(progName) # Get the hexadecimal dump
		headerFile.write("new unsigned char[")
		
		eLen = len(bomb) # Find num of elements
		counter = (eLen)
		rem = (counter) - 1
		progLens.append(eLen) # Append num of elements to list
		
		headerFile.write(str(eLen))
		headerFile.write("]{")

		for i in range(0, counter):
			headerFile.write("0x")
			headerFile.write(bomb[i]) # Write the hexadecimal bytes of the program
			if (i == rem):
				if progName == last:
					headerFile.write("}};")
				else:
					headerFile.write("}, ")
			else:
				headerFile.write(", ")
			
	# Add array to containing program lengths to the header file
	headerFile.write("\n\nunsigned programLengths[] = {")
	
	# The number of programs
	numProgs = 0
	
	# Add to the array in the header file the sizes of each program.
	# That is the first element is the size of program 1, the second element
	# is the size of program 2, etc.
	for progName in execList:
		if progName == last:
			headerFile.write(str(progLens[numProgs]))
			headerFile.write("};")
		else:
			headerFile.write(str(progLens[numProgs]))
			headerFile.write(", ")
			numProgs += 1

	# Write the number of programs.
	headerFile.write("\n\n#define NUM_BINARIES " +  str(len(progNames) - 1))
	
	# Close the header file
	headerFile.close()


############################################################
# Compiles the combined binaries
############################################################
def compileFile():
	
	print("Compiling...")
	os.system("cl binderbackend.cpp")
	

		
	

generateHeaderFile(sys.argv[1:], FILE_NAME)	
compileFile()
