import yaml
from django.core.management.base import BaseCommand
from diplom_app.models import Shop


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('shop1.yaml', 'r') as file:
            shops = yaml.safe_load(file)

        for shop_data in shops:
            shop = Shop()
            shop.name = shop_data['name']
            shop.category = shop_data['category']
            shop.url = shop_data['url']
            shop.user = shop_data['user']
            shop.price = shop_data['price']
            shop.quantity = shop_data['quantity']
            shop.parameters = shop_data['parameters']
            shop.state = shop_data['state']
            shop.save()
