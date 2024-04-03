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

    
    def validate(self, attrs): 

        student_collage_id = attrs['student_collage_id']
        
        # check the student code number
        if len(str(student_collage_id)) <= 9 : 
            raise serializers.ValidationError({
                'message' : 'الرجاء ادخال رقم الكارنية الجامعي صحيح'
            },code=400)
        
        if Post.objects.filter(student_collage_id=student_collage_id).exists() : 
            raise serializers.ValidationError({
                'message' : 'رقم الكارنية الجامعي موجود بالفعل'
            },code=400)
        
        
        return attrs
    

    def to_representation(self, instance:Post):
        data = super().to_representation(instance)
        data['level'] = STR_LEVEL[instance.level]
        return data