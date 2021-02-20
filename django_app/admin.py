from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Player, Comments


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """Представление в административной панели, модели Игроков"""
    list_display = ['pk', 'name', 'surname', 'date_of_birth', 'get_image', 'views', 'get_comments']
    list_display_links = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering = ['pk', 'name', 'surname']
    fields = ['name', 'surname', 'date_of_birth', 'image', 'description']

    def get_image(self, obj):
        """Получение изображения, для отображения в административной панели"""
        if obj.image:
            return mark_safe(f'<img src = "{obj.image.url}" width = "80">')
        else:
            return "Изображение отсутствует"

    def get_comments(self, obj):
        """ Получение количества комментариев, для отображения в административной панели """
        comments = Comments.objects.filter(player=obj.pk).values('pk').count()
        print(comments)
        return comments

    get_image.short_description = "Изображение"
    get_comments.short_description = "Количество комментарии"


@admin.register(Comments)
class PlayerAdmin(admin.ModelAdmin):
    """Представление в административной панели, модели Комментариев"""
    list_display = ['pk', 'player', 'comment_text', 'publication_date']
    list_display_links = ['player', 'comment_text']
    search_fields = ['player__name', 'player__surname', 'comment_text']
    list_filter = ['player']


admin.site.site_header = "Администрирование сайта Футбольной команды"
admin.site.site_title = "Администрирование сайта Футбольной команды"
