pyinstaller --clean --noconsole -n spartan ^
    --add-data="run_wel_check.csv;." ^
    --add-data="fd_res.csv;." ^
    --add-data="type_res.csv;." ^
    --add-data="sr_legacy/sr_legacy.db;sr_legacy" ^
    --add-data="spartan.db;." ^
    --icon=icon/icon.ico ^
    main.py