#gunicorn configuration

command = 'textflows_venv/bin/gunicorn'
pythonpath = 'textflows'
bind = '127.0.0.1:8080'
workers = 3
user = 'mperice'