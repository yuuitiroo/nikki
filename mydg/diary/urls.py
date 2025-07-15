from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),  # ← これを '/' に割り当てる（最上位）
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # ← 認証関連も '/accounts/' に変更
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




#from django.urls import path
#from .import views


#app_name = "diary"
#urlpatterns = [
    #path("", views.index, name="index"),
    #path("page/create/", views.page_create, name ="page_create"),
    #path("pages/" , views.page_list, name="page_list"),
    #path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    #path("page/<uuid:id>/update/", views.page_update, name="page_update"),
    #path("page/<uuid:id>/delete/",views.page_delete, name="page_delete"),
#]