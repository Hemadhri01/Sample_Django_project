from django.urls import reverse, resolve
class TestUrls:
    def test_detail_url(self):
        path = reverse('movies:detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'movies:detail'