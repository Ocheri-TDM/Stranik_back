from django.db import models
from pytils.translit import slugify
from datetime import datetime

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
    title = models.CharField("Название локации", max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Выберите категорию", null=True)
    image = models.ImageField("Фотография", upload_to='photos', blank=True, null=True)
    cost_value = models.IntegerField("Цена (числовое значение)", null=True, blank=True, default=0)
    pop = models.IntegerField("Популярность", default=0)
    date = models.DateTimeField("Дата публикации", default=datetime.now)

    class Meta:
        verbose_name = "Аренда"
        verbose_name_plural = "Аренда"
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.cost_value}$"

    def save(self, *args, **kwargs):
        if self.cost_value is None:
            self.cost_value = 0
        super().save(*args, **kwargs)
