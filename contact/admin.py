from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'category',
        'email',
        'show',
        'created_at',
    )
    # list_filter = ('created_at',)
    list_display_links = ('id', 'first_name',)
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'phone', 'email',)
    list_per_page = 15
    list_max_show_all = 200
    list_editable = ('phone', 'show',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('-id',)
