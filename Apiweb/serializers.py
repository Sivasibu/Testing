from rest_framework import serializers
from .models import Post

class Postserializer(serializers.ModelSerializer):

    created_by =serializers.CharField(source ='created_by.username',read_only=True)
    updated_by =serializers.CharField(source ='updated_by.username',read_only=True)
    class Meta:
        model =Post
        fields = "__all__"
        read_only_fields =('created_by','updated_by')

    def create(self,validated_data):
        validated_data['created_by']=self.context['request'].user
        return Post.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title =validated_data.get('title',instance.title)
        instance.content =validated_data.get('content',instance.content)
        instance.status =validated_data.get('status',instance.status)
        instance.updated_by =self.context['request'].user
        instance.save()
        return instance