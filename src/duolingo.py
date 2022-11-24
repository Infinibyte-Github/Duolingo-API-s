import requests

class ShortAPI:
	def __init__(self, username):
		self.username = username
		self.URL = "https://www.duolingo.com/2017-06-30/users?username={username}"
		self.data = requests.get(self.URL.format(username=self.username))
		self.data_json = self.data.json()['users'][0]
		self.courses = self.Courses(self.data_json)
		self.activelanguage = self.ActiveLanguage(self.data_json['courses'][0])
	
	def streak(self):
		return self.data_json['streak']

	def avatar_small(self):
		return "https:"+self.data_json['picture']+"/large"

	def avatar_large(self):
		return "https:"+self.data_json['picture']+"/xxlarge"

	def userid(self):
		return self.data_json['id']

	def total_crowns(self):
		return sum([course['crowns'] for course in self.data_json['courses']])

	def profile_country(self):
		return self.data_json['profileCountry']

	def has_plus(self):
		return self.data_json['hasPlus']

	def name(self):
		return self.data_json['name']

	def total_xp(self):
		return self.data_json['totalXp']
	

	class Courses:
		def __init__(self, data_json):
			self.data_json = data_json

		def list(self):
			return [course['title'] for course in self.data_json['courses']]

		def list_with_fromLanguage(self):
			return [(course['title'], course['fromLanguage']) for course in self.data_json['courses']]

		def list_with_id(self):
			return [(course['title'], course['id']) for course in self.data_json['courses']]

		def list_raw(self):
			return self.data_json['courses']

		def course_crowns(self, id):
			return self.data_json['courses'][self.list().index(id)]['crowns']

		def number_of_courses(self):
			return len(self.list())

	class ActiveLanguage:
		def __init__(self, data_json):
			self.data_json = data_json

		def title(self):
			return self.data_json['languageData']['title']

		

# class FullAPI:
# 	def __init__(self, username, DummyUsername, DummyPassword):
# 		with requests.Session() as s:
# 			LOGINURL = "https://www.duolingo.com/login?login={username}&password={password}"
# 			login = s.get(LOGINURL.format(username=DummyUsername, password=DummyPassword))

# 			try:
# 				test = login.json()["failure"]
# 				raise Exception("Login failed. Check your username and password.")
# 			except KeyError:
# 				pass

# 			URL = "https://www.duolingo.com/users/{username}"
# 			self.data = s.get(URL.format(username=username))

	# class ActiveLanguage:
	# 	def __init__(self, active_language):
	# 		self.active_language = active_language
		
	# 	def get_name(self):
	# 		return self.active_language['title']

	# 	def get_xp(self):
	# 		return self.active_language['xp']
		
	# 	def get_crowns(self):
	# 		return self.active_language['crowns']