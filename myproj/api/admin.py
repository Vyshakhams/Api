from django.contrib import admin
# Register your models here.
from .models import User, ActivityPeriod, ok

admin.site.register(User)
admin.site.register(ActivityPeriod)
admin.site.register(ok)
