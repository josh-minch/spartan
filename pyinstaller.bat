pyinstaller ^
    --add-data="run_wel_check.csv;." ^
    --add-data="fd_res.csv;." ^
    --add-data="type_res.csv;." ^
    --add-data="sr_legacy/sr_legacy.db;sr_legacy" ^
    main.py