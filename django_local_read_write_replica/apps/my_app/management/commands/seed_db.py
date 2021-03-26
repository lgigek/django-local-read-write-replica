from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--create-super-user", action="store_true", dest="create_super_user", help="Seeds db with a super user"
        )

    def handle(self, *args, **options):
        create_super_user = options["create_super_user"]

        if create_super_user:
            user_model = get_user_model()

            username = "admin"
            password = "test"
            email = "admin@admin.com"

            if user_model.objects.filter(username=username).count() == 0:
                print("Superuser created.")
                user_model.objects.create_superuser(username, email, password)

            else:
                print("Superuser creation skipped.")
