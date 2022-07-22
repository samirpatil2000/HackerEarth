----
# The Gallery CRUD
#### Require

* A GET request to the base URL shoul list ALL Gallery IMages as Cards [DONE]
* A GET request to /show/:id should list details of images. This will be on click of the above Cards [DONE]
* A GET request to /new should show a form for adding new images. The form should contain Image Name, Image URL & Image details as mandory fields to be filled [DONE]
* A POST request to / should submit the above form and add it to database [DONE]
* A GET request to /:id/edit should show a form which has a prefilled Image Name and it must possible to change image URL & Image Details. [DONE]
* A PUT request to /:id/edit should submit the above form and change the approproatew details in the database [DONE]
* A DELETE request to /delete/:id should delete that particular image the database 
* Delete & Edit button should be there in /show/:id [DONE]

#### Additional

* Implement a Pagination feature in the base URL, i.e The base URL [DONE]
* Implement a Search feature in the base URL, i.e it must be possible to search an image by its name across all pages [DONE]
* Implement 5 Unit testcases [DONE more than 5]
* Deployed Code on python anywhere server []

#### [High and Low Level Diagram](https://miro.com/app/board/uXjVOkePgBI=/)
## Installation

[![Python Version](https://img.shields.io/badge/python-3.8.1-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.6-brightgreen.svg)](https://djangoproject.com)



* First, clone the repository to your local machine:

```bash
https://github.com/samirpatil2000/HackerEarth.git
```
* Create & Activate Virtual Environment For Windows

```bash
>> virtualenv env
>> .\env\Scripts\activate
```

* Create & Activate Virtual Environment For MacOs/Linux

```bash
>> virtualenv env
>> . env/bin/activate
```


* Install the requirements:

```bash
>> pip install -r requirements.txt
```

* Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.




#### Contributors



[Back to the top](#The Gallery CRUD)



