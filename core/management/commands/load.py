# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):

        from django.conf import settings
        print('... UPDATING BD ...')
        paths = [
            os.path.join(settings.BASE_DIR, 'core', 'fixtures'),
        ]
        for path in paths:
            fixtures = sorted(os.listdir(path))
            for fixture in fixtures:
                print('\n... LOADING: %s ...' % fixture.split('.')[1])
                call_command('loaddata', fixture)
        print('\n... UPDATE BD ...')
