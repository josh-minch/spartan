pyinstaller --clean --noconfirm --name spartan ^
    --add-data="spartan/run_wel_check.csv;." ^
    --add-data="spartan/fd_res.csv;." ^
    --add-data="spartan/type_res.csv;." ^
    --add-data="spartan/sr_legacy/sr_legacy.db;sr_legacy" ^
    --add-data="spartan/spartan.db;." ^
    --add-data="spartan/cbc.exe;." ^
    --icon=spartan/icon/icon.ico ^
    spartan/main.py