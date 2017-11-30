#!/usr/bin/env python

# Copyright (C) <2014> Janez Kranjc

import os, sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mothra.settings')
    from django.core.management import execute_from_command_line


    from django.conf import settings

    if hasattr(settings, "LATINO_BIN_PATH"):
        import clr
        sys.path.append(settings.LATINO_BIN_PATH)
        import LatinoInterfaces

    execute_from_command_line(sys.argv)
