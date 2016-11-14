from unicodedata import category
from django.core.management.base import BaseCommand, CommandError
from workflows.models import Category, AbstractWidget, AbstractInput, AbstractOutput, AbstractOption
from django.core import serializers
from optparse import make_option
import uuid
import os
import sys
from django.conf import settings
import json
from .export_package import export_package

class Command(BaseCommand):
    args = 'package_name'
    help = 'Exports all packages.'

    def handle(self, *args, **options):
        packages = []
        extern_packages = []
        for app in settings.INSTALLED_APPS:
            if 'workflows.' in app:
                packages.append(app)
            elif app in settings.INSTALLED_APPS_EXTERNAL_PACKAGES:
                extern_packages.append(app)

        for package in packages:
            package_name = package.split('workflows.')[1]
            self.stdout.write("Exporting package "+package_name+"\n")
            export_package(package_name,self.stdout)

        
            
        self.stdout.write("Exporting nltoolkit package \n")
        export_package('tf_core.nltoolkit',self.stdout, dest_folder='C:\\work\\textflows\\tf_core\\nltoolkit')