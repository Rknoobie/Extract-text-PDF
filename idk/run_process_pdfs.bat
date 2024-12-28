@echo off
REM Install the required Python package
echo Installing pypdf...
pip install pypdf

REM Run the Python script
echo Running process_pdfs.py...
python process_pdfs.py

REM Pause to keep the command prompt open
echo Script execution completed. Press any key to exit.
pause