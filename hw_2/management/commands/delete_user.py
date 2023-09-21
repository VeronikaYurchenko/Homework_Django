from django.core.management.base import BaseCommand

from hwo_2.models import User


class Command(BaseCommand):
    help = "Delete user. Command: python manage.py delete_user user_id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.get(pk=pk)
        if user is not None:
            user.delete()
        self.stdout.write(f"User with ID: {pk} deleted.")