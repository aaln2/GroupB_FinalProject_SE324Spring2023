import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        
        
    def test_home_GET(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        
    def test_puzzle_GET(self):#should show him error page
        response = self.client.get(reverse("puzzle"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "error.html")
        
    def test_error_GET(self):
        response = self.client.get(reverse("error"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "error.html")
        
    def test_puzzle_POST(self):
        puzzle_words = SimpleUploadedFile("test.txt", b"Incomplete: Some of us are always meant to be this.\r\nLove: Basis for all of human civilization.", content_type="text")
        response = self.client.post(reverse("puzzle"), {'puzzle_words': puzzle_words})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "puzzle.html")


class FileUploadTestCase(TestCase):
    def test_file_upload_with_valid_extension(self):
        # Create a temporary file with valid content
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
            temp_file.write(b"This is the content of the temporary file.")
            
            # Construct the form data with the temporary file
            form_data = {
                'puzzle_words': open(temp_file.name, 'rb')
            }
            
            # Make a POST request to the view or URL where the form is submitted
            response = self.client.post(reverse('puzzle'), data=form_data)
            
            # Assert that the response status code is 200 (or any other expected status)
            self.assertEqual(response.status_code, 200)
            

    def test_file_upload_with_invalid_extension(self):
        # Create a temporary file with invalid content
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            temp_file.write(b"This is the content of the temporary file.")
            
            # Construct the form data with the temporary file
            form_data = {
                'puzzle_words': open(temp_file.name, 'rb')
            }
            
            # Make a POST request to the view or URL where the form is submitted
            response = self.client.post(reverse('puzzle'), data=form_data)
            
            # Assert that the response status code is not 200 (or any other expected status)
            self.assertNotEqual(response.status_code, 200)

