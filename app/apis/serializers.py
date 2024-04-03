from rest_framework import serializers
from ..models import Post


STR_LEVEL = {
    '1':'فرقة اولي',
    '2':'فرقة ثانية',
    '3':'فرقة ثالثة',
    '4':'فرقة رابعة',
}

class PostSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Post
        fields = "__all__"

    

    def to_representation(self, instance:Post):
        data = super().to_representation(instance)
        data['level'] = STR_LEVEL[instance.level]
        data['posted_at'] = instance.posted_at.date()
        return data