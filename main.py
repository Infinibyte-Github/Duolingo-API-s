#from src.duolingo import FullAPI
from src.duolingo import ShortAPI

# Import the os module to access the environment variables
import os

# Import the dotenv module to access the .env file
from dotenv import load_dotenv
load_dotenv()

# Get the information from the .env file
DUMMYUSERNAME = os.getenv('DummyUsername')
DUMMYPASSWORD = os.getenv('DummyPassword')

#Fapi = FullAPI("Infinibyte", DUMMYUSERNAME, DUMMYPASSWORD)
sapi = ShortAPI("Infinibyte")
print("Streak: ", sapi.streak())
print("Avatar Small: ", sapi.avatar_small())
print("Avatar Large: ", sapi.avatar_large())
print("User ID: " + str(sapi.userid()))
print("Total crowns: " + str(sapi.total_crowns()))
print("Profile country: " + sapi.profile_country())
print("Has plus: " + str(sapi.has_plus()))
print("Name: " + sapi.name())
print("Total xp: " + str(sapi.total_xp()))
print("Number of courses: " + str(sapi.courses.number_of_courses()))
print("Name of active course: " + sapi.activelanguage.title())
print("Learning language: " + sapi.activelanguage.learning_language())
print("Xp of active course: " + str(sapi.activelanguage.xp()))
print("fromLanguage of active course: " + sapi.activelanguage.from_language())
print("Crowns of active course: " + str(sapi.activelanguage.crowns()))
print("ID of active course: " + sapi.activelanguage.id())
# print(sapi.courses.list_raw())
# print(type(sapi.courses.list_with_fromLanguage()))
# print(sapi.courses.list_with_fromLanguage())
# print(sapi.courses.list_with_id())
# print("Courses: " + str(sapi.courses.list_with_fromLanguage()))
# print(sapi.AllLanguages.language_crowns())