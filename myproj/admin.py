from django.contrib import admin
from .models import Article
# Register your models here.
#To easily add or manage articles, register the model in the Django admin:
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title', 'published_date' )
    search_fields=('title', 'summary')
