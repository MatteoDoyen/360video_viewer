set uic=venv\Scripts\pyside2-uic.exe
set files=login_window, upload_window, file_select_window viewer

FOR %%G IN (%files%) DO (
call %uic% UI\%%G.ui -o PY_UI\%%G_ui.py )