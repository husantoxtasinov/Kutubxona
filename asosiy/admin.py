from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    search_fields = ('id','nom','muallif_ism','janr')
    list_filter = ('janr',)
    list_display = ('id','nom','sahifa','janr')
    list_display_links = ('nom','janr')
    list_editable = ('sahifa',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields = ('id','student__ism','kitob__nom')
    list_filter = ('qaytardi',)

admin.site.register(Student)

admin.site.register(Muallif)







