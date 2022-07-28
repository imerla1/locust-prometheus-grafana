from locust import HttpUser, task, between


class JsonAPI(HttpUser):
    wait_time = between(1, 2)
    host = "https://jsonplaceholder.typicode.com"

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_photos(self):
        self.client.get("/photos")
