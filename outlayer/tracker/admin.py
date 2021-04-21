from django.contrib import admin

# Register your models here.
 models = apps.get_models()
 for model in models:
     admin.site.register(model)
 