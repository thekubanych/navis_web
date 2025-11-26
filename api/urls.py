from django.urls import path
from . import views

urlpatterns = [
    path('consultation/', views.ContactCreateView.as_view()),
    path('posts/', views.get_posts),
    path('about/', views.get_about),
    path('projects/', views.get_projects),
    path('tools/', views.get_tools),
    path('reviews/', views.get_reviews),
    path('design/', views.get_design),
    path('vacancy/', views.get_vacancy),
    path('vacancy/apply/', views.VacancyApplicationView.as_view()),
    path('contact/send/', views.ContactCreateView.as_view()),
    path('contact/info/', views.get_contact_info),
    path('viewJob/', views.get_viewjob),

    # Event (обычные)
    path('events/', views.get_events),
    path('event/create/', views.EventCreateView.as_view()),

    # Events (RichText)
    path('events/', views.get_events),
    path('events/<int:pk>/', views.get_event_detail),
]
