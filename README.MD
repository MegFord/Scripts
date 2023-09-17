virtualenv -p /usr/bin/python3.8 venv

source venv/bin activate

python -m pip install .

python stl_convert.py