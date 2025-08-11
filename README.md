# Python-Intern-Elevatelabs
API Day 4 Task
In my program, I created a simple Flask API that manages a list of users stored in memory. I set up five endpoints to handle different actions:
GET /users → I return all the users in my list.
GET /users/<id> → I search through my list to find a user with the given ID and return it, or send a 404 error if I can’t find it.
POST /users → I take the new user’s data from the request, give it a new ID, add it to my list, and return the new user.
PUT /users/<id> → I find the user with the given ID, update its details with the new data from the request, and return the updated user.
DELETE /users/<id> → I remove the user with the given ID from my list and return a confirmation message.
Basically, I built a CRUD API where I can create, read, update, and delete users, all stored in a simple Python list without using any database.
