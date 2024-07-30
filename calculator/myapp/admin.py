from django.contrib import admin
from myapp.models import Service

class Service_admin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

admin.site.register(Service,Service_admin)
# Register your models here.
