"""
URL configuration for mydg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from diary.views_auth import SignupView
from diary.views_auth import DeleteAccountView

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("admin/", admin.site.urls),
    path("diary/", include("diary.urls", namespace="diary")),
    path("", include("diary.urls")),  # ホームを diary に飛ばす場合のみ
    path("delete_account/", DeleteAccountView.as_view(), name="delete_account"),
    path("accounts/", include(("django.contrib.auth.urls", "accounts"), namespace="accounts")),  # accounts.urls が存在しないならこれだけ
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
