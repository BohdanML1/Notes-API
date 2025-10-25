from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, help_text="Автор нотатки")

    title = serializers.CharField(help_text="Заголовок нотатки")
    content = serializers.CharField(help_text="Текст нотатки")
    created_at = serializers.DateTimeField(help_text="Дата створення нотатки", read_only=True)
    updated_at = serializers.DateTimeField(help_text="Дата останнього редагування", read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
