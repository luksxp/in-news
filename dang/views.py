from django.shortcuts import render
from django.views import generic
from dang.models import Category, Link
from django.utils import timezone

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    #num_links = Link.objects.all().count()
    #num_cats = Category.objects.all().count() 
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    category_list = Category.objects.order_by('-views')[:5] 
    page_list = Link.objects.order_by('-views')[:5]
    last_added = Link.objects.order_by('-created_date')[:10]
    context_dict = {'categories': category_list, 
                    'pages': page_list, 
                    'last_added': last_added,
                    'num_visits': num_visits,}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context_dict)
    
def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Link.objects.filter(category=category)\
                    .order_by('-created_date')[:15]
        #pages = Link.objects.order_by('-created_date')
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    # Go render the response and return it to the client.
    return render(request, 'dang/category.html', context_dict)
    


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 15
    
    
class LinkListView(generic.ListView):
    model = Link
    paginate_by = 15
    ordering = ['-created_date']
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from dang.models import Link

class LinkCreate(LoginRequiredMixin, CreateView):
    model = Link
    fields = ['title', 'url', 'category']
    

class LinkUpdate(LoginRequiredMixin, UpdateView):
    model = Link
    fields = ['title', 'url', 'category']

class LinkDelete(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('link')
    
class LinkDetailView(generic.DetailView):
    model = Link
    
