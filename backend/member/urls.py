from django.urls import path
from . import views  # 시블린관계에서는 . 사용

urlpatterns = [
    path('member/signup',views.member_list)
]