from typing import Dict
import time

from celery import shared_task
from category.serializers import CategorySerializer


@shared_task(name='test_celery')
def test_celery(data: Dict) -> None:
    time.sleep(5)
    print(data)


@shared_task(name='create_category')
def create_category(data: Dict) -> None:
    time.sleep(3)
    print('saved category task started!!')
    serializer = CategorySerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    print('saved category task done!!')
