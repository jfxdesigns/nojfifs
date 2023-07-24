@echo off
setlocal enabledelayedexpansion

REM Set the folder path containing the JFIF images (same as the batch file location)
set "source_folder=%~dp0"

REM Change directory to the source folder
cd /d "%source_folder%"

REM Loop through all JFIF images and convert them to PNG
for %%F in (*.jfif) do (
    set "input_file=%%F"
    set "output_file=%%~nF.png"
    echo Converting !input_file! to !output_file!
    magick !input_file! !output_file!
)

echo All JFIF images converted to PNGs.
pause