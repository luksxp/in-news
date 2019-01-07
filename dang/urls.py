from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('link/', views.LinkListView.as_view(), name='link'),    
    
]

urlpatterns += [  
    path('link/create/', views.LinkCreate.as_view(), name='link_create'),
    path('link/<int:pk>/update/', views.LinkUpdate.as_view(), name='link_update'),
    path('link/<int:pk>/delete/', views.LinkDelete.as_view(), name='link_delete'),
]

urlpatterns += [
    
    path('link/<int:pk>', views.LinkDetailView.as_view(), name='link_detail'),
    
]

