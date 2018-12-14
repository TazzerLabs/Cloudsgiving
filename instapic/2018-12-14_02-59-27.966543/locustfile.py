from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
	def on start(self):
		self.client.post("/login". {
			"username": username,
			"password": ""
		})
	@task
	def index(self):
		self.client.get("/")
	@task
	def about(self):
		self.client.get("/upload")

class WebsiteUser(HttpLocust):
	task_Set = WebsiteTasks
	min_wait = 5000
	max_wait = 15000
