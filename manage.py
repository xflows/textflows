#!/usr/bin/env python

# Copyright (C) <2014> Janez Kranjc

import os, sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mothra.settings')
    from django.core.management import execute_from_command_line

    import os
    if os.getenv("COMPUTERNAME") == "MATEJ-PC":
        import clr
        sys.path.append("C:\\work\\tf_latino\\tf_latino\\lib\\bin")
        import LatinoInterfaces

    execute_from_command_line(sys.argv)
