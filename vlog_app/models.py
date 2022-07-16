from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


# Create your models here


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        unique=True
    )
    img = ResizedImageField(
        verbose_name='Пост',
        upload_to='photos/%Y/%m/%d',
        size=[400, 350],
        crop=['middle', 'center']
    )
    description = models.TextField(
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
        verbose_name='Дата создания',
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Дата последнего обновления',
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )

    def __str__(self) -> str:
        return str(self.title)


class Contact(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Название контакта",
        unique=True
    )
    contact_url = models.URLField(
        verbose_name="Ссылка на контакт",
        unique=True
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания контакта',
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Дата последнего обновления контакта',
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True
    )

    class Meta:
        unique_together = ('name', 'contact_url')

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        SITE_INFO['contacts'] = Contact.objects.all()
        return super().save(*args, **kwargs)


class SiteInfo(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Название сайта",
    )
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок сайта",
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание сайта",
    )
    create_date = models.DateTimeField(
        verbose_name='Дата создания контакта',
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Дата последнего обновления контакта',
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name='Активный',
        default=True
    )

    class Meta:
        ordering = ('create_date',)

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs):
        SITE_INFO['site_info'] = self
        return super().save(*args, **kwargs)


# SITE_INFO = {
#     "contacts": Contact.objects.all(),
#     "site_info": SiteInfo.objects.all().first()
# }

SITE_INFO = {
    'contacts': None,
    'site_info': None
}
