from locust import HttpLocust, TaskSet, task
from faker import Faker

fake = Faker()


class UserBehavior(TaskSet):
    def on_start(self):
        pass

    def on_stop(self):
        pass

    def registration(self):
        applicant_name = fake.name()
        pan_name = fake.name()
        params = {'applicant_name': applicant_name, 'pan_name': pan_name}
        url = "getScore"
        self.client.post(url, params)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
