from rest_framework import serializers
from main.models import Product
import asyncio
from scrab.scrabber2 import createApp
 

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'website', 'price_avg', 'sallers', 'name_short_shop', 'name_long_shop', 'created_at',)
        # fields = '__all__'
        read_only_fields = ('name_short_shop', 'name_long_shop', 'sallers', 'price_avg')   
    
    def create(self, validated_data):
        
        products, prices, sold, count, categories_list = asyncio.run(createApp(validated_data['website'], validated_data['name']))
        print(prices)
        validated_data['price_avg'] = round(prices * 6.62)
        validated_data['sallers'] = sold
        validated_data['name_short_shop'] = products[0][0:20]
        validated_data['name_long_shop'] = products[0]


        product = Product.objects.create(**validated_data)

        return product
