import requests

class ShortAPI:
	def __init__(self, username):
		self.username = username
		self.URL = "https://www.duolingo.com/2017-06-30/users?username={username}"
		self.data = requests.get(self.URL.format(username=self.username))
		self.data_json = self.data.json()['users'][0]
		self.courses = self.Courses(self.data_json)
		
	def total_xp(self):
		return self.data_json['totalXp']

	def total_crowns(self):
		return sum([course['crowns'] for course in self.data_json['courses']])

	class Courses:
		def __init__(self, data_json):
			self.data_json = data_json

		def list(self):
			return [course['title'] for course in self.data_json['courses']]

		def list_with_fromLanguage(self):
			return [(course['title'], course['fromLanguage']) for course in self.data_json['courses']]

		def list_with_id(self):
			return [(course['title'], course['id']) for course in self.data_json['courses']]

		def course_crowns(self, id):
			return self.data_json['courses'][self.list().index(id)]['crowns']

class FullAPI:
	def __init__(self, username, DummyUsername, DummyPassword):
		with requests.Session() as s:
			LOGINURL = "https://www.duolingo.com/login?login={username}&password={password}"
			login = s.get(LOGINURL.format(username=DummyUsername, password=DummyPassword))

			try:
				test = login.json()["failure"]
				raise Exception("Login failed. Check your username and password.")
			except KeyError:
				pass

			URL = "https://www.duolingo.com/users/{username}"
			self.data = s.get(URL.format(username=username))

	# class ActiveLanguage:
	# 	def __init__(self, active_language):
	# 		self.active_language = active_language
		
	# 	def get_name(self):
	# 		return self.active_language['title']

	# 	def get_xp(self):
	# 		return self.active_language['xp']
		
	# 	def get_crowns(self):
	# 		return self.active_language['crowns']