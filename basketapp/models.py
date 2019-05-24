from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @cached_property
    def get_items(self):
        return self.user.basket.select_related()

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        return sum(list(map(lambda x: x.quantity, self.get_items)))

    @property
    def total_cost(self):
        "return total cost for user"
        return sum(list(map(lambda x: x.product_cost, self.get_items)))

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

