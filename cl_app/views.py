from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Category, Post
from django.views.decorators.csrf import csrf_exempt
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
        JsonResponse({})
    if(request.method == 'DELETE'):
        Category.objects.filter(id=category_id).delete()
        JsonResponse({})
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
    print('poooooooooooooooosttttttttttttttttttttttttttt', post)
    data = { title: post.title, content: post.content }
    return render(request, 'cl_app/view_post.html', data)
