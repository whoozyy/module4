from django.db import models
from django.contrib import admin

class Advertisement(models.Model):
    title = models.CharField("Заголовок",max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена",max_digits=10,decimal_places=2) #99999999,99
    #999,99 - max_digits = 5,decimal_places = 2
    auction = models.BooleanField("Торг",help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Advertisements(id={self.id},title={self.title},price={self.price})'

    class Meta:
        db_table="advertisements"

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green;font-weight: bold;">Сегодня в {}</span>',created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата обновления")
    def updated_at(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: orange;font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.update_at.strftime("%d.%m.%Y в %H:%M:%S")
