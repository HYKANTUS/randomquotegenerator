@echo on
set loopcount=1000000
:loop
"C:\Users\HP\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\HP\Documents\pythonProject\main.py"
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop