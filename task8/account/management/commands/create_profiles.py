from django.core.management.base import BaseCommand
from account.models import CustomUser, Profile


class Command(BaseCommand):
    help = 'Creating profiles for users without it'

    def handle(self, *args, **options):
        users_without_profile = CustomUser.objects.filter(profile__isnull=True)
        for user in users_without_profile:
            Profile.objects.create(user=user)
            self.stdout.write(f'The profile is created for the user: {user.username}')
        self.stdout.write(self.style.SUCCESS('All profiles have been created'))
