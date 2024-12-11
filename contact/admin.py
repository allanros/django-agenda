from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'created_at',
    )
    # list_filter = ('created_at',)
    ordering = ('-created_at',)
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_per_page = 5
    list_max_show_all = 200
    list_editable = ('phone', )
