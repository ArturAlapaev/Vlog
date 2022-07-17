from django.db import models
from django.db.utils import OperationalError, ProgrammingError
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Заголовок',
        unique=True
    )
    img = ResizedImageField(
        verbose_name='Изображение',
        upload_to='photos/%Y/%m/%d/',
        size=[400, 350],
        crop=['middle', 'center'],

    )
    description = models.TextField(
        max_length=255,
        verbose_name='Комментарий к посту'
    )
    is_draft = models.BooleanField(
        verbose_name='Черновик',
        default=False
    )
    is_delete = models.BooleanField(
        verbose_name='Удален',
        default=False
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'

    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления'
    )
    user_id = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT
    )

    def _str_(self) -> str:
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название контакта'

    )
    contact_url = models.URLField(
        verbose_name='Ссылка на контакт',
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления'
    )
    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True
    )

    class Meta:
        unique_together = ('name', 'contact_url')

    def _str_(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        SITE_INFO["contacts_info"] = Contact.objects.all()
        return super().save(*args, **kwargs)


class SiteInfo(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Название сайта'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок сайта'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание сайта'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления'
    )
    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True
    )

    class Meta:
        ordering = ('create_date',)

    def _str_(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        SITE_INFO["site_info"] = self
        return super().save(*args, **kwargs)

try:
    SITE_INFO = {
        'contacts': Contact.objects.all(),
        'site_info': SiteInfo.objects.all().first()
    }
except OperationalError:
    SITE_INFO = {
        'contacts': None,
        'site_info': None
    }
except ProgrammingError:
    SITE_INFO = {
        'contacts': None,
        'site_info': None
    }