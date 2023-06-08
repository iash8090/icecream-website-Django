from rest_framework import serializers
from .models import ICDetail


class ICDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICDetail
        
# To get all fields use -> '__all__'
#        fields = '__all__'
        fields = ('id', 'name','quantity', 'price', 'Desc')
