from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser, ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        to_update = ShopUser.objects.filter(shopuserprofile__isnull=True)
        print(len(to_update))
        for user in to_update:
            ShopUserProfile.objects.create(user=user)


