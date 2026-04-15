@echo off
title NEXUS TITAN V6 - System Launcher
color 0B
echo ###############################################
echo #       NEXUS TITAN V6 | VISION PROTOCOL      #
echo #       Hardware Optimization: 4GB RAM        #
echo ###############################################
echo.
echo [1/3] Checking Native Python Environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python to run Processor.py
    pause
    exit
)

echo [2/3] Initializing Memory Flush & Cache...
taskkill /f /im chrome.exe >nul 2>&1
taskkill /f /im msedge.exe >nul 2>&1
echo System Memory Purged. Ready for AI Load.

echo [3/3] Launching Offline UI...
start "" "index.html"

echo.
echo ###############################################
echo # SYSTEM ACTIVE: PROTOCOL AMANATDARI ENABLED  #
echo ###############################################
pause
