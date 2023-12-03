from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
