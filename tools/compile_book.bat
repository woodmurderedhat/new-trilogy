@echo off
REM Cutup-Trilogy Book Compilation Tool - Windows Batch Script
REM Usage: compile_book.bat [book_number] [format] [options]

echo.
echo ===============================================
echo   Cutup-Trilogy Book Compilation Tool
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ from python.org
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import yaml" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Installing required packages...
    pip install -r requirements_simple.txt
    if errorlevel 1 (
        echo ❌ Failed to install required packages
        echo Please run: pip install pyyaml
        pause
        exit /b 1
    )
    echo ✅ Packages installed successfully
)

REM Set default values
set BOOK_NUM=%1
set FORMAT=%2

REM Interactive mode if no arguments provided
if "%BOOK_NUM%"=="" (
    echo Select book to compile:
    echo   1 - Fragmented City ^(Book I^)
    echo   2 - Echo Machine ^(Book II^) 
    echo   3 - Reentry ^(Book III^)
    echo.
    set /p BOOK_NUM="Enter book number (1-3): "
)

if "%FORMAT%"=="" (
    echo.
    echo Select export format:
    echo   txt      - Plain text for e-readers
    echo   markdown - Formatted markdown
    echo   json     - Machine-readable data
    echo   all      - All formats ^(recommended^)
    echo.
    set /p FORMAT="Enter format (txt/markdown/json/all): "
)

REM Default to 'all' if still empty
if "%FORMAT%"=="" set FORMAT=all

echo.
echo 🔄 Compiling Book %BOOK_NUM% in %FORMAT% format...
echo.

REM Run the compilation
python compile_book.py --book %BOOK_NUM% --format %FORMAT% --include-metadata

if errorlevel 1 (
    echo.
    echo ❌ Compilation failed
    pause
    exit /b 1
)

echo.
echo ✅ Compilation complete!
echo 📁 Check the exports/ directory for output files
echo.

REM Open exports directory if it exists
if exist "exports" (
    echo Opening exports directory...
    start explorer exports
)

pause