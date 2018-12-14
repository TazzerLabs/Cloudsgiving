from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
	def on_start(self):
		response = self.client.get("/")
		csrftoken = response.cookies['csrftoken']
		self.client.post("/", {
			"username": username,
			"password": ""},
			headers={'X-CSRFToken': csrftoken})

	@task
	def upload(self):
		self.client.get("/upload")
	@task
	def savephoto(self):
		self.client.post('/save-photo',{
		"url": "example.com",
		"baseurl": "example.com",
		"caption": "testing"},
		headers={'X-Requested-With': 'XMLHttpRequest'})

class WebsiteUser(HttpLocust):
	task_set = WebsiteTasks
	min_wait = 5000
	max_wait = 15000
