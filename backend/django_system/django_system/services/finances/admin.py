from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Asset)
admin.site.register(Portfolio)
admin.site.register(DealHistory)
admin.site.register(Item)