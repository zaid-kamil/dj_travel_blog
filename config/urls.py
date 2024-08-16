
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # main views
    path("", main_views.index, name="index"),
    path("login", main_views.login_view, name="login"),
    path("register", main_views.register_view, name="register"),
    path("logout", main_views.logout_view, name="logout"),
    # blog views
    path('blog/all', blog_views.blog_list_view, name='blog_list'),
    path('blog/<int:id>/article', blog_views.article_view, name='article'),
    path('blog/<int:id>/edit', blog_views.edit_article_view, name='edit_article'),
    path('blog/add', blog_views.add_article_view, name='add_article'),
    path('blog/<int:id>/delete', blog_views.delete_article_view, name='delete_article'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)