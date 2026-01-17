@echo off
title VRModz APK
color 5
echo.
echo Beta not released
echo.

for /l %%i in (5,-1,1) do (
    echo Closing in %%i seconds...
    timeout /t 1 >nul
    cls
    echo Beta not released
    echo.
)

exit >nul
