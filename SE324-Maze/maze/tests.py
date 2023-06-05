from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_home_GET(self):
        response = self.client.get(reverse("homeURL"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        
    def test_maze_GET(self):
        response = self.client.get(reverse("mazeURL"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maze.html")
        
    def test_maze_POST(self):
        maze2d = SimpleUploadedFile("test.txt", b"0001101111011101110111000001100001\r\n01110111011111", content_type="text")
        response = self.client.post(reverse("mazeURL"), {'maze2d': maze2d})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maze.html")
        
    