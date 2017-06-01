import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('질문내용', max_length=200)
    pub_date = models.DateTimeField('발행일자')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name='해당 질문',
        on_delete=models.CASCADE)
    choice_text = models.CharField('선택내용', max_length=200)
    votes = models.IntegerField('총 투표수', default=0)

    # Model : DB와 데이터 송수신을 위한 모듈
    # Model에 생성한 클래스에서 사용하는 변수는 DB 테이블의 컬럼과 일치해야 함
    # ForeignKey dml 필드명은 verbose_name 옵션에 넣어줘야 함.
