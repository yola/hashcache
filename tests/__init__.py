import os

# stop django from complaining when we run tests from outside a django project
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
