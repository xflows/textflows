#gunicorn configuration

command = '/home/mperice/.virtualenvs/textflows/bin/gunicorn'
pythonpath = 'textflows'
bind = '127.0.0.1:8080'
workers = 3
user = 'mperice'
timeout = 300