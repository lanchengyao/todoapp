from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete/', views.TodoToggleComplete.as_view()), # 新增
    path('signup/', views.signup), # 新增
    path('login/', views.login),  # 新增这一行
]
