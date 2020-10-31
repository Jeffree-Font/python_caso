from django.contrib import admin
from .models import Cliente,Insumos,SliderHindex,MisionVision,Galeria


class ClientesAdmin(admin.ModelAdmin):
    list_display=['name','apellido','email','username','password']
    search_fields=['name','username']
    list_filter=['name']
    list_per_page=10
class InsumosAdmin(admin.ModelAdmin):
    list_display=['name','precio','descripcion','stock']
    search_fields=['name','precio']
    list_filter=['name','precio']
    list_per_page=10

# Register your models here.

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Insumos, InsumosAdmin)
admin.site.register(SliderHindex)
admin.site.register(MisionVision)
admin.site.register(Galeria)