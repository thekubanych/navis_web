from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
import requests

from .models import *
from .serializers import *

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
CHAT_ID = settings.CHAT_ID

# ---------------------- Event ----------------------
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        event = serializer.save()
        message = (
            f'📅 Новое мероприятие добавлено!\n\n'
            f'Название: {event.title}\n'
            f'Описание: {event.description}\n'
            f'Дата: {event.date}\n'
            f'Время: {event.time}\n'
            f'Адрес: {event.location}\n'
            f'Статус: {"✅ Ожидается" if event.status == "upcoming" else "❌ Прошло"}'
        )

        send_message_url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        send_photo_url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto'

        if event.image:
            try:
                with open(event.image.path, 'rb') as photo:
                    requests.post(send_photo_url, data={'chat_id': CHAT_ID, 'caption': message}, files={'photo': photo})
            except Exception as e:
                print(f"❌ Ошибка при отправке фото в Telegram: {e}")
                requests.post(send_message_url, data={'chat_id': CHAT_ID, 'text': message})
        else:
            requests.post(send_message_url, data={'chat_id': CHAT_ID, 'text': message})

@api_view(['GET'])
def get_events(request):
    serializer = EventSerializer(Event.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, context={'request': request})
        return Response(serializer.data)
    except Event.DoesNotExist:
        return Response({'error': 'Мероприятие не найдено'}, status=404)


# ---------------------- Post ----------------------
@api_view(['GET'])
def get_posts(request):
    serializer = PostSerializer(Post.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

# ---------------------- About ----------------------
@api_view(['GET'])
def get_about(request):
    serializer = AboutSerializer(About.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

# ---------------------- Project ----------------------
@api_view(['GET'])
def get_projects(request):
    serializer = ProjectSerializer(Project.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

# ---------------------- Tool ----------------------
@api_view(['GET'])
def get_tools(request):
    serializer = ToolSerializer(Tool.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

# ---------------------- Review ----------------------
@api_view(['GET'])
def get_reviews(request):
    serializer = ReviewSerializer(Review.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

# ---------------------- Design ----------------------
@api_view(['GET'])
def get_design(request):
    serializer = DesignSerializer(Design.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)

# ---------------------- Vacancy ----------------------
@api_view(['GET'])
def get_vacancy(request):
    vacancy = Vacancy.objects.first()
    if vacancy:
        serializer = VacancySerializer(vacancy, context={'request': request})
        return Response(serializer.data)
    return Response({'message': 'Нет активных вакансий'}, status=404)

class VacancyApplicationView(generics.CreateAPIView):
    queryset = VacancyApplication.objects.all()
    serializer_class = VacancyApplicationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        app = serializer.save()
        message = (
            f'🧾 Новый отклик на вакансию!\n\n'
            f'Имя: {app.name}\n'
            f'Email: {app.email}\n'
            f'Телефон: {app.phone}\n'
            f'LinkedIn: {app.linkedin or "Не указано"}'
        )
        send_message_url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        send_document_url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument'

        if getattr(app, 'resume', None):
            try:
                with open(app.resume.path, 'rb') as doc:
                    requests.post(send_document_url, data={'chat_id': CHAT_ID, 'caption': message}, files={'document': doc})
            except Exception as e:
                print(f"❌ Ошибка при отправке резюме: {e}")
                requests.post(send_message_url, data={'chat_id': CHAT_ID, 'text': message})
        else:
            requests.post(send_message_url, data={'chat_id': CHAT_ID, 'text': message})

# ---------------------- Contact ----------------------
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        contact = serializer.save()
        message = f'📩 Новая контактная заявка!\nИмя: {contact.name}\nТелефон: {contact.phone}\nИнтересует: {contact.message}'
        requests.post(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', data={'chat_id': CHAT_ID, 'text': message})

# ---------------------- Contact Info ----------------------
@api_view(['GET'])
def get_contact_info(request):
    info = ContactInfo.objects.first()
    if info:
        serializer = ContactInfoSerializer(info, context={'request': request})
        return Response(serializer.data)
    return Response({'message': 'Информация не найдена'}, status=404)

# ---------------------- View Job ----------------------
@api_view(['GET'])
def get_viewjob(request):
    serializer = ViewJobSerializer(ViewJob.objects.all(), many=True, context={'request': request})
    return Response(serializer.data)
