from django.http import HttpResponse, Http404
from client.forms import PostCreateForm
from django.shortcuts import redirect, render, resolve_url
from django.views.generic import TemplateView, CreateView, View
from client.models import User
from main.models import Post

import random


  


class MainIndex(TemplateView):
    template_name = "main/index.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = Post.objects.order_by("?").all()
        
        context['posts'] = Post.objects.all()

        return context



class PostLike(View):
    def get(self, request, pk, type):
        try:
            d = Post.objects.get(id=pk)
        except:
            return redirect('main:http_404')

        if type == 'u':
            d.like += 1
        elif type == 'd':
            d.dislike += 1

        d.save()

        return HttpResponse('{}/{}'.format(d.like,d.dislike))



class CreatePost(View):
    def get(self, request):
        return render(request, 'main/post_form.html', {
            'form': PostCreateForm
        })

    def post(self, request):
        
        form = PostCreateForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            Post(**form.cleaned_data, user=request.user).save()
            return redirect("main:index")

        return render(request, "main/post_form.html", {
            'form': form
        })

def video_viewer(request, id):
    try:
        d = Post.objects.get(id=id)
        d.shown += 1
        d.save()

    except Post.DoesNotExist:
        return redirect('main:http_404')
    
    list = Post.objects.all()
    


    
    return render(request, 'main/video_viewer.html',{
        'd':d,
        'list':list
    })

class Search(TemplateView):
    template_name = 'main/index.html'
    def get_context_data(self,**kwargs):
        context=super(Search,self).get_context_data(**kwargs)
        context['subject']=Post.objects.filter(subject__icontains=self.request.GET.get('query',''))

        return context

    def post(self,request):
        pass    


def profileView(request, id):

    list = Post.objects.filter(user_id=id).all()

    
    return render(request, 'main/profile_view.html',{
        
        'list':list
    })

def delete(request,id):
    d = Post.objects.filter(id=id).delete()
    return redirect("main:index")
    return render(request,'main/index.html',{
        'd':d
    })

class http_404(TemplateView):
    template_name='main/404.html'