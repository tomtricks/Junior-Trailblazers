from audioop import reverse
from turtle import pos
from unicodedata import category
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Category, Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name='home.html'
    ordering=['-publication_date']
    
    # ordering=['-id']


    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)
    # To get category in nav bar ,To get this category in every page just copy this method and paste it in need page
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'
# just shows the category view
    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
       
        #to get and show likes
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
       
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model=Post
    # Below form_class indicates that it should use the custom form from Postform class
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__' #it takes all the fields No need for postform class(custom form)
    # fields = ('title','body')

class UpdatePostView(UpdateView):
    model=Post
    # TO need an some change salone use Editform class from models
    form_class=EditForm
    template_name = 'update_post.html'
    # fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model=Category
    # Below form_class indicates that it should use the custom form from Postform class
    # form_class=PostForm
    template_name='add_category.html'
    fields='__all__' #it takes all the fields No need for postform class(custom form)
    # fields = ('title','body')

def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats.replace('-',' '))
    

    return render(request,'categories.html',{'cats':cats.title().replace('-',' '), 'category_post':category_post})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',
    {'cat_menu_list':cat_menu_list})

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    # Unlike and like
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked=True
    
    # post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))
    #also form articledetailsview to show how many likes in top function
