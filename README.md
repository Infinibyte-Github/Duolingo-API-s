# Duolingo-API-s
Attempt to make the Duolingo API's accesible from within Python

## 2 API's
There are two different api's: 
- a short one which doesn"t require a login, but it only gives basic information like streak and courses
- a long one that requires authentication but gives back more information, especially detailed information about the current course

To get full functionality you need to use both of the api's since the second one only shows the courses with the same base language as the current one, while the other one gives all the courses but provides less information in general.