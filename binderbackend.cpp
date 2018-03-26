#include <string>
#include "codearray.h"
#include <stdlib.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <iostream>
#include <windows.h>
using namespace std;

int main()
{
	/* Go through the binaries */
	for (int progCount = 0; progCount < NUM_BINARIES; ++progCount)
	{
		// Open the file and write the bytes of the first program to the file.
		// These bytes are found in codeArray[progCount]

		/* Generate the file names */
		string tmp = "railgun";
		tmp += to_string(progCount);
		tmp += ".exe";
		const char* biri = tmp.c_str();

		/* Open the file for writing binary values */
		FILE* fp = fopen(biri, "wb");
		if (!fp) /* Make sure the file was opened */
		{
			perror("fopen");
			exit(-1);
		}

		/* Write to the program */
		if (fwrite(codeArray[progCount], sizeof(char), programLengths[progCount], fp) < 0)
		{
			perror("fwrite");
			exit(-1);
		}

		/* Close the file */
		fclose(fp);

		// Create process
		STARTUPINFO info = { sizeof(info) };
		PROCESS_INFORMATION processInfo;
		if (CreateProcess(biri, NULL, NULL, NULL, TRUE, 0, NULL, NULL, &info, &processInfo))
		{
			WaitForSingleObject(processInfo.hProcess, INFINITE);
			CloseHandle(processInfo.hProcess);
			CloseHandle(processInfo.hThread);
		}
	}
}
