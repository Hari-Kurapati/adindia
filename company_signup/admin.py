from django.contrib import admin
from .models import Advertisers, Ads_catagory

# Register your models here.
class Ads_catagoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'ad_name']

class AdvertisersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    'company_name',
    'company_phone',
    'company_email', 
    'ad_price',
    'ad_name']


admin.site.register(Advertisers, AdvertisersAdmin)
admin.site.register(Ads_catagory, Ads_catagoryAdmin)
