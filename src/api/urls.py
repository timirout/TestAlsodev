from django.urls import path
from api.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDestroyView, AuthorCreateView


urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("create_author/", AuthorCreateView.as_view(), name="create_author"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("<int:pk>/", ProductUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductDestroyView.as_view(), name="delete"),
]
