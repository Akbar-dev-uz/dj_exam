from django.urls import path
from event import views as event_views

urlpatterns = [
    path('', event_views.home, name='home'),
    path('create/', event_views.create_event, name='create_event'),
    path('update/<int:event_id>/', event_views.update, name='update_event'),
    path('view/<int:event_id>/', event_views.view, name='view_event'),
    path('delete/<int:event_id>/', event_views.delete, name='delete'),
]

