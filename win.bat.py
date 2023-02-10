@echo off

rem Set the environment
set PYTHONPATH=%PYTHONPATH%;C:\Users\spani\Python\

rem Run postman_api.py
start C:\Users\spani\Python\pythonw.exe C:\Users\spani\Documents\Postman\Tests\postman_api.py

rem Run test_com5.py
start C:\Users\spani\Python\pythonw.exe C:\Users\spani\Documents\Postman\Tests\test_com5.py

rem Run test_com4.py
start C:\Users\spani\Python\pythonw.exe C:\Users\spani\Documents\Postman\Tests\test_com4.py

pause
