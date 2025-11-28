from django.urls import path
from . import views

urlpatterns = [
    # Consultation / Contact
    path('consultation/', views.ContactCreateView.as_view()),
    path('contact/send/', views.ContactCreateView.as_view()),
    path('contact/info/', views.get_contact_info),

    # Posts / About / Projects / Tools / Reviews / Design
    path('posts/', views.get_posts),
    path('about/', views.get_about),
    path('projects/', views.get_projects),
    path('tools/', views.get_tools),
    path('reviews/', views.get_reviews),
    path('design/', views.get_design),

    # Vacancy
    path('vacancy/', views.get_vacancy),
    path('vacancy/apply/', views.VacancyApplicationView.as_view()),

    # View Job
    path('viewJob/', views.get_viewjob),

    # Events
    path('events/', views.get_events),  # жалпы окуялар
    path('events/<int:pk>/', views.get_event_detail),  # окуянын деталдары
    path('event/create/', views.EventCreateView.as_view()),  # жаңы окуя кошуу
]
