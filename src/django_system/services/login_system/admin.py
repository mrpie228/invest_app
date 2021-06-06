from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)

admin.site.site_title = "Invest App"
admin.site.site_header = "Invest App"
