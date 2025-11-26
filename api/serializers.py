from rest_framework import serializers
from .models import *

class AbsoluteUrlImageMixin(serializers.ModelSerializer):
    """Миксин для конвертации ImageField в абсолютный URL"""
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        for field in self.Meta.model._meta.fields:
            if 'ImageField' in str(field.get_internal_type()):
                img_field = getattr(instance, field.name)
                if img_field:
                    rep[field.name] = request.build_absolute_uri(img_field.url) if request else img_field.url
        return rep

class EventSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class PostSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AboutSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ProjectSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ToolSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class ReviewSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class DesignSerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'

class VacancySerializer(AbsoluteUrlImageMixin, serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyApplication
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class ViewJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewJob
        fields = '__all__'
