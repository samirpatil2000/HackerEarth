from django.test import TestCase
from django.urls import reverse
from gallery.models import Image
from utils.constant import URLS

IMAGE_URL = 'https://www.frostscience.org/wp-content/uploads/2021/03/GSFC_20171208_Archive_e000528_orig.jpg'


# Create your tests here.
class TestImageListView(TestCase):

    @classmethod
    def setUpTestData(cls):
        for author_id in range(22):
            Image.objects.create(
                name=f'Image {author_id}',
                detail=f'The detail of Image {author_id}',
                url=IMAGE_URL
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_nine(self):
        response = self.client.get(reverse(URLS.IMAGE_LIST))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        # checking here number of pagination
        self.assertEqual(len(response.context['images']), 9)

    def test_lists_all_images(self):
        response = self.client.get(reverse(URLS.IMAGE_LIST) + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        # checking here on third page there should be exact 4 image objects
        self.assertEqual(len(response.context['images']), 4)
