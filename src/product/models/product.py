import uuid

from django.db import models

from core.models import BaseModel




class Product(BaseModel):
    name = models.CharField(max_length=255, )
    description = models.TextField(null=True, blank=True)
    sku = models.UUIDField(editable=False, default=uuid.uuid4, unique=True, )
    price = models.DecimalField(max_digits=10, decimal_places=2, )
    image = models.TextField(null=True, blank=True)
    category = models.ForeignKey(to='category.Category', on_delete=models.PROTECT)

    class Meta:
        db_table = 'products'

    def __str__(self):
        #return str(self.sku)
        return (self.name)
