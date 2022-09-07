from django.test import TestCase

from schedulerApp.task import reverse_request_title
from .models import Request
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from .singleton import SingletonClass

# Create your tests here.
class RequestTest(TestCase):
    def setUp(self):
        self.request = Request(title='test', scheduledDateTime='2021-09-01 00:00:00', status='pending')
        self.request.save()
        self.scheduler = BackgroundScheduler()

    def test_request_title(self):
        self.assertEqual(self.request.title, 'test')

    def test_request_scheduledDateTime(self):
        self.assertEqual(self.request.scheduledDateTime, '2021-09-01 00:00:00')

    def test_request_status(self):
        self.assertEqual(self.request.status, 'pending')

    def test_request_changeStatus(self):
        self.request.changeStatus('completed')
        self.assertEqual(self.request.status, 'completed')

    def test_request_str(self):
        self.assertEqual(str(self.request), 'test')
    
    def test_request_get(self):
        response = self.client.get('/schedulerApp/request')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'test')
        self.assertEqual(response.data[0]['scheduledDateTime'], '2021-09-01T00:00:00+02:00')
        self.assertEqual(response.data[0]['status'], 'pending')
    
    def test_request_post(self):
        response = self.client.post('/schedulerApp/request', {'title': 'test2', 'scheduledDateTime': (datetime.now() + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')})
        self.assertEqual(response.status_code, 200)

    def test_task_reverse_request_title(self):
        response = reverse_request_title(self.request.id)
        self.assertEqual(response.title, 'tset')
        self.assertEqual(response.status, 'completed')

    def test_request_post_invalid(self):
        response = self.client.post('/schedulerApp/request', {'title': 'test2', 'scheduledDateTime': (datetime.now() - timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')})
        self.assertEqual(response.status_code, 400)
       
    def test_get_job(self):
        response = self.client.post('/schedulerApp/request', {'title': 'test3', 'scheduledDateTime': (datetime.now() + timedelta(seconds=5)).strftime('%Y-%m-%d %H:%M:%S')})
        singletonClass = SingletonClass()
        scheduler = singletonClass.scheduler
        for job in scheduler.get_jobs():
            print("Job Name: ", job.name)
            self.assertEqual(job.name, str(response.data['id']))
            self.assertEqual(job.func, reverse_request_title)