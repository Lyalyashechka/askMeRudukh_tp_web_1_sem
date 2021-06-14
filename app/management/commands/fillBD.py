from django.core.management.base import BaseCommand, CommandError
from app.models import User, Tag, Like, Question, Answer


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--users', nargs='+')
        parser.add_argument('tags', nargs='+')

    def fill_users(self, count):
        last_user = User.objects.all().last()
        if last_user is None:
            last_id = 0
        else:
            last_id = last_user.id
        for i in range(count):
            current_user = User.objects.create_user(f'User{last_id + 1 + i}')
            current_user.id = last_id + 1 + i

    def fill_tags(self, count):
        for i in range(count):
            tags = Tag(name=i)
            tags.save()

    def handle(self, *args, **options):
        if options['users']:
            self.fill_users(100)
        if options['tags']:
            self.fill_tags(100)



