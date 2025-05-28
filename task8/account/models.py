import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as PilImage
from io import BytesIO


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)

        user.set_password(password)

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if extra_fields.setdefault('is_staff', True) is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.setdefault('is_superuser', True) is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')

        return self.create_user(username, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=32)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


def image_size_validator(image):
    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(
            message='Image size more than 2MB',
            code='Big image size'
        )


def image_resolution_validator(image):
    img = PilImage.open(image)
    if img.width < 100 or img.height < 100:
        raise ValidationError(
            message='Too small resolution',
            code='too small resolution'
        )


def image_aspect_ratio_validator(image):
    img = PilImage.open(image)
    aspect_ratio = img.width / img.height
    if aspect_ratio < 1 or aspect_ratio > 1.25:
        raise ValidationError(
            message='Wrong aspect ratio',
            code='wrong aspect ratio'
        )


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True,
                               validators=[image_size_validator, image_resolution_validator,
                                           image_aspect_ratio_validator])
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=512, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.pk and self.avatar:
            old_avatar = Profile.objects.get(pk=self.pk).avatar
            if old_avatar and old_avatar != self.avatar and os.path.exists(old_avatar.path):
                os.remove(old_avatar.path)
        super().save(*args, **kwargs)

    # def crop_image(self):
    #     if self.avatar:
    #         img = PilImage.open(self.avatar.path)
    #         width, height = img.size
    #         if img.height != img.width:
    #             min_side = min(width, height)
    #             max_side = max(width, height)
    #             first = (max_side - min_side) // 2
    #             second = first + min_side
    #             # sides order: left, top, right, bottom
    #             if min_side == width:
    #                 sides = [0, first, min_side, second]
    #             else:
    #                 sides = [first, 0, second, min_side]
    #             img_format = img.format
    #             img = img.crop(tuple(sides))
    #             buffer = BytesIO()
    #             img.save(buffer, format=img_format)
    #             buffer.seek(0)
    #
    #             return InMemoryUploadedFile(file=buffer, field_name=None, name=self.avatar.name,
    #                                         content_type=self.avatar.file.content_type, size=buffer.tell(),
    #                                         charset=None)
    #     return self.avatar


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
