from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from users import views as user_views
from django.urls import path, include, re_path
from django.conf.urls.static import static, serve
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete'),

    path('', blog_views.PostListView.as_view(template_name='home.html'), name='blog-home'),
    path('user/<str:username>', blog_views.UserPostListView.as_view(template_name='user_posts.html'), name='user-posts'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(template_name='post_detail.html'), name='post-detail'),
    path('post/<int:pk>/update/', blog_views.PostUpdateView.as_view(template_name='post_form.html'), name='post-update'),
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post-delete'),
    path('post/new/', blog_views.PostCreateView.as_view(template_name='post_form.html'), name='post-create'),
    path('about/', blog_views.about, name='blog-about'),


    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
