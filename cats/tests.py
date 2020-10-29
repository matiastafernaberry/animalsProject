from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory

from . import views


class CatViewTestCase(TestCase):
    longMessage = True    
    def test_get(self):
        status_code = 200
        view_class = views.CatRandomView
        
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = views.CatRandomView.as_view()(req, *[], **{})
        self.assertEqual(resp.status_code, 200)
