from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pics/", default="profile_pics/default.jpg", blank=True, null=True)

    def __str__(self):
        return self.user.username
class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or self.name != Category.objects.get(pk=self.pk).name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Rent(models.Model):
    title = models.CharField("Название локации", max_length=30)
    text = models.TextField("Дополнительная информация по локации:", default="Default text")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Выберите категорию", null=True)
    cost_value = models.IntegerField("Цена (числовое значение)", null=True, blank=True, default=0)
    pop = models.IntegerField("Популярность", default=0)
    date = models.DateField("Время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренда"

    def __str__(self):
        return f"{self.title} - {self.cost_value}$"

    def save(self, *args, **kwargs):
        if self.cost_value is None:
            self.cost_value = 0
        super().save(*args, **kwargs)

class RentImage(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Фотография", upload_to='photos')
    is_main = models.BooleanField("Главное фото", default=False)

    class Meta:
        verbose_name = "Фотография локации"
        verbose_name_plural = "Фотографии локации"

    def __str__(self):
        return f"Фото для {self.rent.title}"



class Ad(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Активное'),
        ('sold', 'Продано'),
        ('expired', 'Истекло')
    ])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.title


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ViewedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    viewed_at = models.DateTimeField(auto_now_add=True)

    content_object = GenericForeignKey("content_type", "object_id")

    def viewed_object(self):
        return self.content_object

class FavoriteAd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_ads')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'ad')