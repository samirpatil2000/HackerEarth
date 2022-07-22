from django.test import TestCase
from gallery.models import Image

IMAGE_URL = 'https://www.frostscience.org/wp-content/uploads/2021/03/GSFC_20171208_Archive_e000528_orig.jpg'


# Create your tests here.
class TestImageModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.image = Image.objects.create(
            name='My Image',
            detail='This is my image',
            url=IMAGE_URL
        )

    def test_create_image_object(self):
        self.assertEqual(self.image.name, 'My Image')
        self.assertEqual(self.image.detail, 'This is my image')
        self.assertEqual(self.image.url, IMAGE_URL)

    def test_image_str(self):
        self.assertEqual(str(self.image), 'My Image')
