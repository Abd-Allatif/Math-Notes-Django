from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .utils import analyze_image
from io import BytesIO
import base64
from PIL import Image

class ImageAnalysisView(APIView):
    def post(self, request):
        try:
            serializer = ImageDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            image_data = data['image'].split(",")[1]
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
            responses = analyze_image(image, data['dict_of_vars'])
            return Response({
            "message": "Image processed",
            "data": responses,
            "status": "success"
            })
        except  Exception as e:
            return Response({'Error':e},status=status.HTTP_400_BAD_REQUEST)
