from django.contrib import admin

from .models import *


class DisplayAsset(admin.ModelAdmin):
    list_display = ('kode_field','nama_field','Gas_Target','Oil_Target','OilUOM','GasUOM')



class DisplayInputAsset(admin.ModelAdmin):
    list_display = (
    	# 'Kode_field'
    	'date',
    	'nama_field',
        'Gas_Target',
        'Gas_Target',
        'Oil_Target',
        'InputOil_Target',
        'InputGas_Target',
    	)
    # class Meta :
    # 	model = Input_Asset2

    # def get_kode_field(self,obj):
    # 	return obj.author.kode_field

    # get_kode_field.admin_order_field = 'kode_field'


# admin.site.register(Asset1,DisplayAsset)
# admin.site.register(Input_Asset1,DisplayInputAsset)

admin.site.register(Asset1,DisplayAsset)
admin.site.register(Input_Asset1,DisplayInputAsset)
admin.site.register(Asset2,DisplayAsset)
admin.site.register(Input_Asset2,DisplayInputAsset)
admin.site.register(Asset3,DisplayAsset)
admin.site.register(Input_Asset3,DisplayInputAsset)
admin.site.register(Asset4,DisplayAsset)
admin.site.register(Input_Asset4,DisplayInputAsset)
admin.site.register(Asset5,DisplayAsset)
admin.site.register(Input_Asset5,DisplayInputAsset)