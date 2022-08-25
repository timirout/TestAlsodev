from rest_framework.serializers import ModelSerializer, ListField, ImageField
from api.models import Product, Image, Author


# Сериалайзер для считывания данных о всех Авторах (Сделан для просмотра данных о авторе в продукте)
class AuthorReadSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


# Сериалайзер для создания Автора
class AuthorCreateSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email']


# Сериалайзер для считывания данных о всех продуктах
class ProductReadSerializer(ModelSerializer):

    author_id = AuthorReadSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name_product', 'price_product', 'images', 'author_id']


# Сериалайзер для создания Продукта
class ProductСreateSerializer(ModelSerializer):

    images = ListField(child=ImageField(max_length=100000, allow_empty_file=False, use_url=False))

    class Meta:
        model = Product
        fields = ['name_product', 'price_product', 'images', 'author_id']

    def create(self, validated_data):
        name_product = validated_data['name_product']
        price_product = validated_data['price_product']
        author_id = validated_data['author_id']
        images = self.context['request'].FILES.getlist('images')

        product = Product(
            name_product=name_product, price_product=price_product, author_id=author_id)
        product.save()

        Image.objects.bulk_create([Image(product_id=product, image=image) for image in images])

        return validated_data


# Сериалайзер для обновления Продукта
class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name_product', 'price_product', 'images']


# Сериалайзер для удаления Продукта
class ProductDeleteSerializer(ProductUpdateSerializer):
    class Meta(ProductUpdateSerializer.Meta):
        pass
