The bonus binder runs on the Windows platform (tested with 7) and needs the following:

1. Windows Powershell 1.0 (Should be automatically installed in Windows)

2. Microsoft Visual Studio 13.0 with the C++ compiler (Tested with 13.0, but higher should be fine)

3. Python 3.4 (Tested with 3.4, but lower/higher should be fine)

Note: You may need to configure windows enviroment PATH for Python to give sys arguments

Maku sure all relevant files are in the same working directory!
 
How to execute the program:

1. Start Developer Command Prompt for VS2013 (automatically sets up the command line environment)

Alternatively: Run command prompt and navigate to where-ever Microsoft Visudo Studio XX.X\VC\bin is installed to.
Run vcvars32.bat and proceed to the next step

2. "cd" to your working directory that has all the bonus files and enter the following

3. binderBonus.py <prog1> <prog2> ... <progN> (e.g. binderBonus.py helloWorld.exe king.exe)

4. Wait until it finishes! This step may take several minutes (especially on slow machines).

5. If successful, the output file should be binderbackend.exe

Note: Consider to disable any antivirus during testing