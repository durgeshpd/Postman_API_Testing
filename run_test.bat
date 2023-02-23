@echo off

rem Set the environment
set PYTHONPATH=%PYTHONPATH%;C:\Users\spani\Python\

rem Run postman_api.py
start /B C:\Users\spani\Python\pythonw.exe C:\Users\spani\Documents\Durgesh\Postman_API\postman_api.py

rem Run test_com5.py
start /B C:\Users\spani\Python\pythonw.exe C:\Users\spani\Documents\Durgesh\Postman_API\test_com5.py

rem Run test_com4.py
start /B C:\Users\spani\Python\pythonw.exe C:\Users\spani\Documents\Durgesh\Postman_API\test_com4.py

pause
