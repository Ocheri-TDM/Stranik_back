from django.contrib import admin
from .models import Category, Rent, RentImage
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Ad, FavoriteAd

admin.site.register(Category)
class RentImageInline(admin.TabularInline):
    model = RentImage
    extra = 1

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    inlines = [RentImageInline]


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'owner', 'date_posted', 'status')  # Исправлено "user" -> "owner", "created_at" -> "date_posted"
    search_fields = ('title', 'owner__username')  
    list_filter = ('date_posted', 'status')  

@admin.register(FavoriteAd)
class FavoriteAdAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad')  
    search_fields = ('user__username', 'ad__title')