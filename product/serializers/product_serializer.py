from product.models.category import Category
from rest_framework import serializers
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(
        read_only=True, many=True
    )  # mais de um produto para uma determinada ordem
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)
        return product
