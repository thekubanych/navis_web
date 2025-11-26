from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
import os

class Post(models.Model):
    img = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)
    ckeditor = RichTextUploadingField()

    class Meta:
        verbose_name = 'Наши услуги'
        verbose_name_plural = 'Наши услугии'

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    position = models.CharField(max_length=150, verbose_name='Должность / компания')
    description = models.TextField(verbose_name='Отзыв')
    img = models.ImageField(upload_to='reviews/', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} — {self.position}'

class Design(models.Model):
    img = models.ImageField(upload_to='Design')
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайны'

    def __str__(self):
        return self.title


def validate_resume(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.docx']
    if ext.lower() not in valid_extensions:
        raise ValidationError("Можно загружать только PDF или DOCX файлы")


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    description = RichTextUploadingField(verbose_name="Описание вакансии")

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title


class VacancyApplication(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    linkedin = models.URLField(verbose_name="Ссылка на соцсеть", blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", verbose_name="Резюме", blank=True, null=True, validators=[validate_resume])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики"

    def __str__(self):
        return f"{self.name} — {self.email}"



class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    message = models.TextField(verbose_name='Что вас интересует?')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'kontact zayavki'
        verbose_name_plural = 'kontact zayavki'

    def __str__(self):
        return f'{self.name} - {self.phone}'


class ContactInfo(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    schedule = models.CharField(max_length=100, verbose_name='Режим работы')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Кontact info'
        verbose_name_plural = 'kontaktnaya info'

    def __str__(self):
        return 'Контакты компании'

class ViewJob(models.Model):
    LEVEL_CHOICES = [
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    ]

    WORK_TYPE_CHOICES = [
        ('office', 'Полный рабочий день'),
        ('remote', 'Удаленно'),
        ('hybrid', 'Гибридный график'),
    ]

    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Уровень")
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, verbose_name="График работы")

    def __str__(self):
        return f"{self.title} ({self.level})"


class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Предстоящий'),
        ('completed', 'Завершённый'),
        ('canceled', 'Отменённый'),
        ('past', 'Прошедший'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название события')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='events/', verbose_name='Фото')
    date = models.CharField(max_length=100, verbose_name='Дата')
    time = models.CharField(max_length=50, verbose_name='Время')
    location = models.CharField(max_length=255, verbose_name='Адрес')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='upcoming', verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'meropriyatie'
        verbose_name_plural = 'meropriyatiya'


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=(
        ('upcoming', 'Будущее'),
        ('past', 'Прошедшее'),
    ))

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'meropriyatie'
        verbose_name_plural = 'meropriyatiye'



class About(models.Model):
    img = models.ImageField(upload_to='about/', verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

class Project(models.Model):
    img = models.ImageField(upload_to='projects/', verbose_name='Фото проекта')
    title = models.CharField(max_length=255, verbose_name='Название проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'nashi proekti'

    def __str__(self):
        return self.title

class Consultation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Что вас интересует')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    class Meta:
        verbose_name = 'zayavka'
        verbose_name_plural = 'zayavki'

    def __str__(self):
        return f'{self.name} ({self.phone})'

class Tool(models.Model):
    img = models.ImageField(upload_to='tools/', verbose_name='Логотип')
    title = models.CharField(max_length=255, verbose_name='Название технологии')
    description = RichTextUploadingField(null=True, blank=True)


    class Meta:
        verbose_name = 'instrument'
        verbose_name_plural = 'instrumenti'

    def __str__(self):
        return self.title

