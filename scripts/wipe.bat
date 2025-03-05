@echo off

set script_dir=%cd%
cd ..

set parentdir=%cd%

cd /d %parentdir%

if not exist "venv" (
    python -m venv venv
    venv\Scripts\pip install .
)

venv\Scripts\python src\autozenith.wipe.py
