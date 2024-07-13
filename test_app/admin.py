from typing import Any
from django.contrib import admin
from .models import  Sentences , Dictionary , MasoudDictionary,ErfanDictionary
# # Register your models here.


class CustomSentences(admin.ModelAdmin):
    list_display = ["text","related_word"]
    search_fields = ["text","related_word"]


class InlineSentences(admin.TabularInline):
    model = Sentences
    fields = ["text","related_word"]
    extra = 0


class CustomDictionary(admin.ModelAdmin):
    inlines = [InlineSentences]
    list_display = ['word','mean','level']
    list_editable = ['level']
    search_fields = ['word','mean']
    list_filter = ['level']
    
    

class CustomMasoudDictionary(CustomDictionary):
    list_filter = ['level',]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author__first_name='Masoud')
    

class CustomErfanDictionary(CustomDictionary):
    list_filter = ['level','is_show']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(author__first_name='Erfan')
    



admin.site.register(Sentences,CustomSentences)
admin.site.register(Dictionary,CustomDictionary)
admin.site.register(MasoudDictionary,CustomMasoudDictionary)
admin.site.register(ErfanDictionary,CustomErfanDictionary)

