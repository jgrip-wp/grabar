from io import BytesIO
import os
from django.core.files.base import ContentFile
from django.forms import Form, ModelForm
from PIL import Image
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'number',
            'name',
            'name_kana',
            'email',
            'department',
            'thumbnail',
        )

    def clean_thumbnail(self):
        data = self.cleaned_data['thumbnail']
        if data is None:
            return data

        # reshape as a rectangle image
        img = Image.open(data)
        if img.width != img.height:
            half_size = min(img.width, img.height) / 2
            center = (int(img.width / 2), int(img.height / 2))
            img = img.crop((
                center[0] - half_size,
                center[1] - half_size,
                center[0] + half_size,
                center[1] + half_size
            ))

        # resize
        if img.width > 90:
            img = img.resize((90, 90))

        new_content = BytesIO()
        img.save(new_content, format='PNG')
        file_name = os.path.splitext(data.name)[0] + '.png'
        return ContentFile(new_content.getvalue(), name=file_name)
