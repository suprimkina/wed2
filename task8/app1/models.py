from django.db import models
from django.conf import settings


class ProgLang(models.Model):
    prog_lang_name = models.CharField(max_length=64)

    def __str__(self):
        return self.prog_lang_name


class Application(models.Model):
    fio = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    bday = models.DateField()
    sex = models.CharField(max_length=5)
    biography = models.TextField(max_length=512, blank=True)
    prog_langs = models.ManyToManyField(ProgLang)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return (f"fio: {self.fio}, telephone: {self.telephone}, email: {self.bday},"
                f" sex: {self.sex}, biography: {self.fio}, prog_langs: {self.prog_langs}")
