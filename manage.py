#!/usr/bin/env python

# Copyright (C) <2014> Janez Kranjc

import os, sys

if __name__ == '__main__':
    import clr
    sys.path.append("C:\\Users\\Roman\\PycharmProjects\\textflows\\workflows\\textflows_dot_net\\bin")
    import LatinoClowdFlows

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mothra.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
