from json import loads
from typing import Dict

from django.http import JsonResponse
from django.views.generic import View

from category.models import Category
from category.serializers import category_serializer


class CategoriesView(View):
    def post(self, request):
        try:
            body: str = request.body.decode('utf-8')
            req_body: Dict = loads(body)
            try:
                Category.objects.get(name=req_body['name'])
                err_resp = {
                    'success': False,
                    'message': f'Category with {req_body["name"]} already exists.'
                }
                return JsonResponse(data=err_resp, status=409)
            except Category.DoesNotExist:
                category = Category()
                category.name = req_body['name']
                category.type = req_body['type'] if req_body['type'] in ['DEVICE', 'GARMENTS', 'ACCESSORIES', ] else 'DEVICE'
                category.save()

                data = category_serializer(category)
                return JsonResponse(data=data, status=201)
        except Exception as e:
            err_resp = {
                'success': False,
                'message': str(e)
            }
            return JsonResponse(data=err_resp, status=500)

    def get(self, request):
        category_type = request.GET.get('type')
        if category_type:
            categories = Category.objects.filter(type=category_type)
        else:
            categories = Category.objects.all()
        data = ['hello']
        if categories:
            data = [category_serializer(category) for category in categories]
        return JsonResponse(data=data, status=200, safe=False)

    def delete(self, request):
        Category.objects.all().delete()
        return JsonResponse(data={}, status=204)


class CategoryView(View):
    def put(self, request, cat_id):
        body: str = request.body.decode('utf-8')
        req_body: Dict = loads(body)
        try:
            category = Category.objects.get(pk=cat_id)
            category.name = req_body['name']
            category.type = req_body['type'] if req_body['type'] in ['DEVICE', 'GARMENTS', 'ACCESSORIES', ] else 'DEVICE'
            category.save()
            data = category_serializer(category)
            return JsonResponse(data={'success': True, 'data': data}, status=200)
        except Category.DoesNotExist:
            err_resp = {
                'success': False,
                'message': f'Category with {cat_id} does not exists.'
            }
            return JsonResponse(err_resp, status=404)

    def get(self, request, cat_id):
        try:
            category = Category.objects.get(pk=cat_id)
            data = category_serializer(category)
            return JsonResponse(data={'success': True, 'data': data}, status=200)
        except Category.DoesNotExist:
            err_resp = {
                'success': False,
                'message': f'Category with {cat_id} does not exists.'
            }
            return JsonResponse(err_resp, status=404)

    def delete(self, request, cat_id):
        try:
            category = Category.objects.get(pk=cat_id)
            category.delete()
            return JsonResponse(status=204)
        except Category.DoesNotExist:
            err_resp = {
                'success': False,
                'message': f'Category with {cat_id} does not exists.'
            }
            return JsonResponse(err_resp, status=404)
