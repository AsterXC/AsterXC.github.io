@echo off

set "d="
set "p="

cls
echo PS %d%^> ^.^\run
echo Serving HTTP on :: port %p% (http://127.0.0.1:%p%/) ...

cd /d %d%
python -m http.server %p% -d %d% 1>out.log 2>err.log
exit /b 0