from django.contrib import admin
# from .models import related models
from .model import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 5
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = [['name', 'type', 'make', 'year']
    inlines = [CarModelInline]
# Register models here
admin.site.register(CarModelInline, CarModelAdmin, CarMakeAdmin)
admin.site.register(CarMake)
admin.site.register(CarModel)