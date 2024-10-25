@echo off
REM Get the drive letter where the batch file is located
set usb_drive=%~d0

REM Set the path for the Python script on the USB drive
set script_path=%usb_drive%\merge_takeout.py

REM Run the Python script and log output
python %script_path% > %usb_drive%\log.txt 2>&1

REM Optional: add a pause to see the output before closing
pause
