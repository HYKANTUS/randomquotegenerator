@echo on
:: Loopcount set to 450 as that seems to be close to the limit (you may change it from 450-500 at your own risk of not being able to use the InstaBot library)
set loopcount=450
:loop

:: First quote for python.exe location                          | Second quote for python script location.
"C:\Users\HP\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\HP\Documents\pythonProject\main.py"

set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
