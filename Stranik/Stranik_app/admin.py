from django.contrib import admin
from .models import Category, Rent, RentImage

admin.site.register(Category)
class RentImageInline(admin.TabularInline):
    model = RentImage
    extra = 1

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    inlines = [RentImageInline]

