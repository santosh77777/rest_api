from django.urls import path
from . import views


urlpatterns = [
    path('', views.MemberGenericAPIView.as_view()),
    path('api/members/', views.MemberGenericAPIView.as_view()),
    path('api/member/<int:id>/', views.MemberGenericAPIView.as_view()),

]
 