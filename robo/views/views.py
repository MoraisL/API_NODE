from django.shortcuts import render
from rest_framework import generics
from robo.models.clp import ViewSettings
from robo.serializers.serializers import ViewSettingsSerializer

class ViewSettingsListCreate(generics.ListCreateAPIView):
    queryset = ViewSettings.objects.all()  # Use o modelo atualizado
    serializer_class = ViewSettingsSerializer

def render_pag_html(request):
    # Obtém a última requisição
    last_item = ViewSettings.objects.latest('id')
    # Serializa a última requisição
    serializer = ViewSettingsSerializer(last_item)
    # Renderiza o template com os dados da última requisição
    return render(request, 'pag.html', {'data': [serializer.data]})
