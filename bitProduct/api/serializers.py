from rest_framework import serializers
from main.models import Product
import asyncio
from scrab.scrabber2 import createApp


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'website', 'price_avg', 'sallers', 'name_short_shop', 'name_long_shop')
        # fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'name_short_shop', 'name_long_shop', 'sallers', 'price_avg')   
    
    def create(self, validated_data):
        
        products, prices, sold, count, categories_list = asyncio.run(createApp(validated_data['website'], validated_data['name']))
        validated_data['sallers'] = len(sold)
        validated_data['name_short_shop'] = products[0][0:20]
        validated_data['name_long_shop'] = products[0]


        product = Product.objects.create(**validated_data)

        return product
