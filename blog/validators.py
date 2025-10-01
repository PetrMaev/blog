from rest_framework import serializers

FORBIDDEN_WORDS = ['ерунда', 'глупость', 'чепуха']


class TitleValidator:
    __fields__ = ['title']

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        title = dict(value).get(self.field)
        for word in FORBIDDEN_WORDS:
            if word.lower() in title.lower():
                raise serializers.ValidationError(
                    f'Слово "{word}" не может содержаться в заголовке поста'
                )
