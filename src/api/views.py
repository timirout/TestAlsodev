from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from api.serializers import ProductReadSerializer, ProductСreateSerializer, ProductUpdateSerializer, \
    ProductDeleteSerializer, AuthorCreateSerializer

from api.models import Product


class AuthorCreateView(CreateAPIView):
    serializer_class = AuthorCreateSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer


class ProductCreateView(CreateAPIView):
    serializer_class = ProductСreateSerializer


class ProductUpdateView(RetrieveUpdateAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()


class ProductDestroyView(RetrieveDestroyAPIView):
    serializer_class = ProductDeleteSerializer
    queryset = Product.objects.all()
