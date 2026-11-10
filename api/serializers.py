from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created_at', 'completed']

# 新增：用于一键切换完成状态的序列化器
class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        # 这里把其他字段设为只读，因为切换状态时不需要接收前端传来的内容
        read_only_fields = ['title', 'memo', 'created_at', 'completed']