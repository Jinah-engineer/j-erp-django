from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
# ajax
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import Size, Category, Product


# size

# modal view
@csrf_exempt
def size_get(request):
    size_id = request.GET['size_id']
    size = Size.objects.get(size_id = size_id)
    data = model_to_dict(size)
    print(data)

    return JsonResponse(data, content_type="application/json")


# page view
def size_view(request):
    # size table 조회
    rsBoard = Size.objects.all().order_by('-size_id')
    # category table 조회
    category = Category.objects.all().order_by('category_big')

    product_dict = {}
    # 존재하는 카테고리 수만큼 반복
    for i in category:
        # 카테고리 id가 일치하는 product
        product = Product.objects.filter(category_id=i.category_id)
        product_list = list()
        for j in product:
            # 카테고리에 해당하는 '상품이름' 리스트 생성
            product_list.append(j)
        # i -> 카테고리, product_list -> 해당하는 품목 리스트
        # {i[0]:product_list, i[1]:product_list...i[n]:product_list} dictionary
        product_dict[i] = product_list

    if Size.objects.first() is not None:
        last_id = Size.objects.last().size_id + 1
    else:
        last_id = 1

    context = {}

    context["last_id"] = last_id
    context["size_table"] = rsBoard
    context["product_dict"] = product_dict

    return render(request, 'size.html', context)


# size insert
def size_insert(request):
    size_product = request.GET['size_product']
    print(size_product)
    size_name = request.GET['size_name']
    size_price = request.GET['size_price']
    if size_product and size_name and size_price != "":
        rows = Size.objects.create(product_id_id=size_product, size_name=size_name, size_price=size_price)
        return redirect('information:size_view')
    else:
        return redirect('information:size_view')


# size update
def size_update(request):
    size_id = request.GET['size_id']
    size_product = request.GET['size_product']
    size_name = request.GET['size_name']
    size_price = request.GET['size_price']

    try:
        size = Size.objects.get(size_id = size_id)
        if size_product != "":
            size.product_id = size_product
        if size_name != "":
            size.size_name = size_name
        if size_price != "":
            size.size_price = size_price

        try:
            size.save()
            return redirect('information:size_view')
        except ValueError:
            return HttpResponse({"success": False, "msg":"에러가 발생했습니다"})

    except ObjectDoesNotExist:
        return HttpResponse({"success": False, "msg": "정보가 존재하지 않습니다"})


# size delete
def size_delete(request):
    size_id = request.GET['size_id']
    rows = Size.objects.get(size_id=size_id).delete()

    return redirect('information:size_view')