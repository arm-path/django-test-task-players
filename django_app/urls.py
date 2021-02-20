from django.urls import path

from django_app.views import PlayerListView, PlayerDetailView

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('player/<slug:slug>/', PlayerDetailView.as_view(), name='player_detail'),
]
