from django.contrib import admin
# Added manually
from app1.models import Contact, ICDetail


# use of this class is to show the column name in Admin panel using list_display tuple
class ICDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')

# Register your models here.
# Added manually

admin.site.register(Contact)
admin.site.register(ICDetail, ICDetailAdmin)