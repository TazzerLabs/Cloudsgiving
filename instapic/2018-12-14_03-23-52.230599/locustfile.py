from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
	def on_start(self):
		self.client.post("/", {
			"username": username,
			"password": ""
	})

	@task
	def about(self):
		self.client.get("/upload")

class WebsiteUser(HttpLocust):
	task_Set = WebsiteTasks
	min_wait = 5000
	max_wait = 15000
