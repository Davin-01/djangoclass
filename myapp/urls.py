from django.urls import path


from . import views

urlpatterns=[
    path('index.html',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('products.html',views.products,name='products'),
    path('store.html',views.store,name='store'),
]
