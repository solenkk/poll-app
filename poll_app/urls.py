from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.PollListCreateView.as_view(), name='poll-list-create'),
    path('polls/<int:poll_id>/vote/', views.vote_on_poll, name='vote-on-poll'),
    path('polls/<int:poll_id>/results/', views.poll_results, name='poll-results'),
]