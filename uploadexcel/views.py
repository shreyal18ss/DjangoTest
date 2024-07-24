from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import ExcelData
from .serializers import ExcelDataSerializer
import pandas as pd

from .models import ExcelData

def data_grid(request):
    data = ExcelData.objects.all()
    return render(request, 'uploadexcel/data_grid.html', {'data': data})

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        # Render the input form on GET request
        return render(request, 'uploadexcel/input.html')

    def post(self, request, *args, **kwargs):
        excel_file = request.FILES.get('myfile')
        if not excel_file:
            return Response({"error": "No file provided"}, status=400)
        
        df = pd.read_excel(excel_file, engine='openpyxl')
        records = df.to_dict('records')
        for record in records:
            serializer = ExcelDataSerializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # return Response(serializer.errors, status=400)
                return Response({"message": "File uploaded and data saved successfully"}, status=201)
        return Response({"message": "File uploaded and data saved successfully"}, status=201)