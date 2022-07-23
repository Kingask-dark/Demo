from django.contrib import admin
from DemoApp.models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('productCategory', 'productName' , 'productCost')
    list_editable = ('productCost', )
    list_filter = ('productCategory','productCost')
    search_fields = ('productCategory', 'productName')
    fieldsets = (
        (None, {
            'fields': (
                'productCategory',
                'productName',
                'productCost',
                'productImage',
                'productDescription'
            )
        }),
    )


admin.site.register(Products,ProductAdmin)
