from rest_framework import serializers
from main.models import Product
import asyncio
from parser.scrabber2 import createApp


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'website')
        # fields = '__all__'
    
    def create(self, validated_data):
        
        loop = asyncio.get_event_loop()
        products, prices, sold = loop.run_until_complete(createApp(validated_data['website'])) 
        
        product = Product.objects.create(**validated_data)

        return product
