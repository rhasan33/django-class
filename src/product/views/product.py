from json import loads
from typing import Dict

from django.http import JsonResponse
from django.views.generic import View

from product.models import Product
from product.serializers import product_serializer


class ProductsView(View):

    def get(self, request,):
        #data = ['hello']
        #return JsonResponse(data=data, status=200, safe=False)
        data=[]

        product_name = request.GET.get('name')
        if product_name:
            products = Product.objects.filter(name=product_name)
        else:
            products = Product.objects.all()
        data = []
        if products:
            data = [product_serializer(product) for product in products]
        return JsonResponse(data=data, status=200, safe=False)


    def post(self, request):
        try:
            body: str = request.body.decode('utf-8')
            req_body: Dict = loads(body)

            try:
                Product.objects.get(name=req_body['name'])
                err_resp = {
                    'success': False,
                    'message': f'Category with {req_body["name"]} already exists.'
                }
                return JsonResponse(data=err_resp, status=409)

            except Product.DoesNotExist:

                product = Product()

                product.name = req_body['name']
                product.description = req_body['description']
                product.sku = req_body['sku']
                product.price = req_body['price']
                product.image = req_body['image']
                product.category_id = req_body['category']



                product.save()

                data = product_serializer(product)
                return JsonResponse(data=data, status=201)
        except Exception as e:
            err_resp = {
                'success': False,
                'message': str(e)
            }
            return JsonResponse(data=err_resp, status=500)


    # def delete(self, request):
    #     Category.objects.all().delete()
    #     return JsonResponse(data={}, status=204)

# #
# # class CategoryView(View):
# #     def put(self, request, cat_id):
# #         body: str = request.body.decode('utf-8')
# #         req_body: Dict = loads(body)
# #         try:
# #             category = Category.objects.get(pk=cat_id)
# #             category.name = req_body['name']
# #             category.type = req_body['type'] if req_body['type'] in ['DEVICE', 'GARMENTS', 'ACCESSORIES', ] else 'DEVICE'
# #             category.save()
# #             data = category_serializer(category)
# #             return JsonResponse(data={'success': True, 'data': data}, status=200)
# #         except Category.DoesNotExist:
# #             err_resp = {
# #                 'success': False,
# #                 'message': f'Category with {cat_id} does not exists.'
# #             }
# #             return JsonResponse(err_resp, status=404)
# #
# #     def get(self, request, cat_id):
# #         try:
# #             category = Category.objects.get(pk=cat_id)
# #             data = category_serializer(category)
# #             return JsonResponse(data={'success': True, 'data': data}, status=200)
# #         except Category.DoesNotExist:
# #             err_resp = {
# #                 'success': False,
# #                 'message': f'Category with {cat_id} does not exists.'
# #             }
# #             return JsonResponse(err_resp, status=404)
# #
# #
# #
