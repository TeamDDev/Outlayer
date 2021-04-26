from django.contrib import admin
from tracker.models import Profile, Records
# Register your models here.
'''
models = apps.get_models()
for model in models:
    admin.site.register(model)
'''

admin.site.register(Profile)
admin.site.register(Records)