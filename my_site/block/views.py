from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator , EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .froms import EmailPostFrom
from django.core.mail import send_mail

# Create your views here.
'''
def post_list(request):
    post_list= Post.objects.all()  #get data
    paginator = Paginator(post_list,2) # Show 2 objects per page
    page = request.GET.get('page',1) # to get page and assign first page if null
    try:
        #current_page_objects = paginator.get_page(page)
        current_page_objects = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_page_objects = paginator.page(paginator.num_pages)

    except PageNotAnInteger:
         # If page is not an integer, deliver first page.
        current_page_objects = paginator.page(1)   


    #context = {'current_page_objects': current_page_objects}

    return render(request, 'blog/post/list.html', {'current_page_objects':current_page_objects})

   '''
class PostListView(ListView):
   """
   alternative Post list view

   """
   model = Post
   context_object_name = 'posts'
   paginate_by = 2
   template_name = 'blog/post/list.html'
    #def post_detail(request,year,month,day,post):
def post_detail(request,year,month,day,post):
    #method 1
   # try:
       # post=Post.objects.get(id=id)
   # except Post.DoesNotExist:
       # raise Http404("no post found")  
    #return render(request,'block/post/detail.html',{'post':post})  
    post = get_object_or_404(Post,status=Post.Status.PUBlISHED,
                             slug=post,
                             publish_year=year,
                             publish_month=month,
                             publish_day=day)
    #post = get_object_or_404(Post,id=id,status=Post.Status.PUBlISHED)                        
    return render(request,'blog/post/detail.html',{'post':post})

def home(request):
  return render(request,'home.html')


#def about(request):
   #return render(request,'about.html')

def post_share(request ,post_id):
   post = get_object_or_404(Post,id=post_id,status=Post.Status.PUBlISHED)
   sent = False
   if request.method == 'POST':
      #from was submitted
      form = EmailPostFrom(request.POST)
      if form.is_valid():
         #form fields passed validation
         cd = form.cleaned_data
         post_url = request.build_absolute_uri(post.get_absolute_url())
         subject = f"{cd['name']} recomands you read {post.title}"
         message = f"read{post.title} at {post_url} \n {cd['name']} \s comments: {cd['comments']}"
         send_mail(subject , message , 'acc.mohamed190@gmail.com' , [cd['to']])
         sent = True
   else:
      form = EmailPostFrom()
      return render(request ,'blog/post/share.html', {'post':post ,'form':form ,'sent':sent})

      
           






      
