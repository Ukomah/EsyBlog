from django.urls import path
from .views import Index, DetailArticleView

urlpatterns = [
    path('', Index.as_view(), name='index' ),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    

]