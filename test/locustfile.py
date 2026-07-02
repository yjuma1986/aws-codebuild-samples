from locust import HttpUser, task
class LoadTestUser(HttpUser):
    @task
    def get_post(self):
        self.client.get("/posts/1")