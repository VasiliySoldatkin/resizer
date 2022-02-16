from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ImageSerializer, ImageResizeSerializer
from .models import ImagesModel
from .utils.image_utils import get_cleaned_image_name
from io import BytesIO
from rest_framework.decorators import action
from PIL import Image


class ImagesDetailViewSet(ModelViewSet):
    queryset = ImagesModel.objects.select_related('parent_picture')
    serializer_class = ImageSerializer

    @action(detail=True, methods=['POST'])
    def resize(self, request, pk):
        sizes = (int(request.data['height']), int(request.data['width']))
        image = self.get_object()
        serializer = self.get_serializer(image, data=request.data)
        serializer.is_valid(raise_exception=True)
        path = image.picture.path
        fp = BytesIO()
        name = get_cleaned_image_name(image.picture.name)
        try:
            with Image.open(path) as file_instance:
                resized_image = file_instance.resize(size=sizes, reducing_gap=3)
                resized_image.save(fp, format=file_instance.format)
                image.picture.save(name, fp)
        except OSError:
            return Response({'error': "Can't open image file"})

        self.perform_update(serializer)

        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'resize':
            return ImageResizeSerializer
        else:
            return ImageSerializer

# Create your views here.
