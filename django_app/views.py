from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from django_app.forms import CommentsForm
from django_app.models import Player


class PlayerListView(ListView):
    """ Класс представления списка игроков футбольной команды """
    template_name = 'django_app/player_list.html'
    context_object_name = 'players'

    def get_context_data(self, **kwargs):
        """ Добавление дополнительного контекста к представлению списка """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список игроков футбольной команды'
        return context

    def get_queryset(self):
        if self.request.GET.get('search'):
            """ Поиск по имени или фамилии игрока """
            search_name = self.request.GET.get('search')
            players = Player.objects.filter(Q(name__icontains=search_name) | Q(surname__icontains=search_name))
            if not players:
                return {'error': 'Поиск не дал результатов ...'}
            return players
        else:
            return Player.objects.all()


class PlayerDetailView(FormMixin, DetailView):
    """ Класс представления игрока команды """
    model = Player
    form_class = CommentsForm
    template_name = 'django_app/player_detail.html'
    context_object_name = 'player'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        player = Player.objects.get(slug=self.kwargs['slug'])
        player.views += 1
        player.save()
        context['title'] = player
        return context
