
from django.urls import path
from .import views
from .views_auth import SignupView

app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name ="page_create"),
    path("pages/" , views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    path("page/<uuid:id>/update/", views.page_update, name="page_update"),
    path("page/<uuid:id>/delete/",views.page_delete, name="page_delete"),
    #path('diary/', views.p, name='diary'),  # '/diary/' に対応するビュー
    path("signup/" , SignupView.as_view(), name="signup")
]