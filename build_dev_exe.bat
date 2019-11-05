pyinstaller --clean --noconfirm --name spartan ^
    --add-data="run_wel_check.csv;." ^
    --add-data="fd_res.csv;." ^
    --add-data="type_res.csv;." ^
    --add-data="sr_legacy/sr_legacy.db;sr_legacy" ^
    --add-data="spartan.db;." ^
    --add-data="cbc.exe;." ^
    --icon=icon/icon.ico ^
    main.py