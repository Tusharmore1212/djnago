from django.contrib import admin
from storedata.models import Store

class Store_admin(admin.ModelAdmin):
    list_display=('fname','lname','email','password','cpassword')
admin.site.register(Store,Store_admin)
# Register your models here.
