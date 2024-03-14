from rest_framework import serializers
from robo.models.clp import ViewSettings

class ViewSettingsSerializer(serializers.ModelSerializer):
    request_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', source='created_at', read_only=True)

    class Meta:
        model = ViewSettings
        fields = ['sensor', 'botao', 'liga_robo', 'reset_contador', 'valor_contagem', 'request_time']
