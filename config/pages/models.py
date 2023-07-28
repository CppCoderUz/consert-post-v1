from django.db import models



class BannerImage(models.Model):
    image = models.ImageField(upload_to='images/banner', verbose_name='Banner uchun rasm')

    def __str__(self) -> str:
        return self.image.name
    
    class Meta:
        verbose_name = 'Banner rasmi '
        verbose_name_plural = '1. Banner rasmlari'


UZ = 'uz'
RU = 'ru'
EN = 'en'
LANGUAGE_CHOICES = (
    (UZ, UZ),
    (RU, RU),
    (EN, EN),
)

class Consert(models.Model):
    name = models.CharField(max_length=200, verbose_name="Konsert nomi yoki artist ismi")
    image = models.ImageField(upload_to='images/consert', verbose_name="Konsert uchun rasm yuklang")
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Sana")
    language = models.CharField(max_length=10, verbose_name="Ma'lumot chiqariladigan til", choices=LANGUAGE_CHOICES, default=UZ)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Konsert '
        verbose_name_plural = '2. Konsertlar'




class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tadbir nomi")
    image = models.ImageField(upload_to='images/event', verbose_name="Tadbir uchun rasm yuklang")
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Sana")
    description = models.TextField(null=True, blank=True, verbose_name="Tadbir haqida qisqacha ma'lumot")
    language = models.CharField(max_length=10, verbose_name="Ma'lumot chiqariladigan til", choices=LANGUAGE_CHOICES, default=UZ)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Tadbir '
        verbose_name_plural = '3. Tadbirlar'
        