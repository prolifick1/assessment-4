from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

def list_categories(request):
    all_categories = Category.objects.all().values()
    return render(request, 'cl_app/list_categories.html', context= { "categories" : all_categories } )

@csrf_exempt
def add_category(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        newCategory = Category(name=body['name'])
        newCategory.save()
        return JsonResponse({})
    return render(request, 'cl_app/add_category.html')

def view_category(request, category_id):
    posts = Post.objects.filter(category=category_id)
    data = { "posts": posts }
    return render(request, 'cl_app/view_category.html', data)

@csrf_exempt
def edit_category(request, category_id):
    category_name = Category.objects.filter(id=category_id).get().name
    data = { "category_name": category_name }
    if(request.method == 'PUT'):
        body = json.loads(request.body)
        Category.objects.filter(id=category_id).update(name=body['name'])
        return JsonResponse({})
    if(request.method == 'DELETE'):
        Category.objects.filter(id=category_id).delete()
        return JsonResponse({})
    return render(request, 'cl_app/edit_category.html', data)


@csrf_exempt
def add_post(request, category_id):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        c = Category.objects.get(id=category_id)
        newPost = Post(title=body['title'], content=body['content'], category=c)
        newPost.save()
        return JsonResponse({});
    return render(request, 'cl_app/add_post.html')

def view_post(request, category_id, post_id):
    post = Post.objects.get(id=post_id)
    data = { "post_title": post.title, "post_content": post.content }
    return render(request, 'cl_app/view_post.html', data)

@csrf_exempt
def edit_post(request, category_id, post_id):
    post_title = Post.objects.filter(id=post_id).get().title
    post_content = Post.objects.filter(id=post_id).get().content
    data = { "post_title": post_title, "post_content": post_content }
    if(request.method == 'GET'):
        return render(request, 'cl_app/edit_post.html', data)
    if(request.method == 'POST'):
        body = json.loads(request.body)
        updatedPost = Post.objects.filter(id=post_id).update(title=body['title'], content=body['content'])
        return JsonResponse({});
    if(request.method == 'DELETE'):
        Post.objects.filter(id=post_id).delete()
        return JsonResponse({})

@csrf_exempt
def categories(request):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        new_category = Category(name=body['name'])
        new_category.save()
    categories = Category.objects.all().values()
    return JsonResponse(list(categories), safe=False)

@csrf_exempt
def category(request, category_id):
    if(request.method == 'DELETE'):
        deleted = Category.objects.filter(id=category_id)
        Category.objects.filter(id=category_id).delete()
        return JsonResponse(list(deleted.values()), safe=False)
    if(request.method == 'PUT'):
        body=json.loads(request.body)
        Category.objects.filter(id=category_id).update(name=body['name'])
        updated_category = Category.objects.filter(id=category_id).values()
        data = list(updated_category.values())
        return JsonResponse(data, safe=False)
    category = Category.objects.filter(id=category_id).values()
    return JsonResponse(list(category), safe=False)

@csrf_exempt
def posts(request, category_id=None):
    if(request.method == 'POST'):
        body = json.loads(request.body)
        new_post = Post(title=body['title'], content=body['content'])
        new_post.save()
    if(category_id):
        selected_posts = Post.objects.filter(id=category_id)
        return JsonResponse(list(selected_posts), safe=False)
    all_posts = Post.objects.all().values()
    return JsonResponse(list(all_posts), safe=False)

@csrf_exempt
def post(request, post_id):
    if(request.method == 'DELETE'):
        Post.objects.filter(id=post_id).delete()
        data = serializers.serialize('json', Post.objects.all())
        return HttpResponse(data, content_type='application/json')
    if(request.method == 'PUT'):
        body = json.loads(request.body)   
        selected_post = Post.objects.filter(id=post_id).update(title=body['title'], content=body['content'])
    data = serializers.serialize('json', Post.objects.filter(id=post_id))
    return HttpResponse(data, content_type='application/json')
