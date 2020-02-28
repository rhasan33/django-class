from typing import Dict

from product.models import Product

from category.serializers.category import category_serializer

def product_serializer(product: Product) -> Dict:


    data: Dict = {
        'id': product.id,
        'name': product.name,
        'sku': product.sku,
        'price': product.price,
        'image': product.image,
        'category': product.category_id,

        'created_at': str(product.created_at),
        'updated_at': str(product.updated_at),
    }

    return data
