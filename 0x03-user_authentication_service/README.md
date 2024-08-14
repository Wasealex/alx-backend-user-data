How to declare API routes in a Flask app

## How to get and set cookies

To get and set cookies in your application, you can use the following steps:

1. **Getting Cookies**: To retrieve cookies from a request, you can access the `request.cookies` object. This object contains key-value pairs of all the cookies sent with the request.

   ```python
   cookies = request.cookies
   ```

   You can then access individual cookies by their name:

   ```python
   session_id = cookies.get('session_id')
   ```

2. **Setting Cookies**: To set cookies in a response, you can use the `response.set_cookie()` method. This method takes the name and value of the cookie as arguments, along with optional parameters such as the expiration time and domain.

   ```python
   response.set_cookie('session_id', '123456789', expires=datetime.now() + timedelta(days=7), domain='example.com')
   ```

   Note that the `expires` parameter is used to set the expiration time of the cookie. In the example above, the cookie will expire in 7 days.

## How to retrieve request form data

To retrieve form data from a request, you can use the following steps:

1. **Using Flask**: If you are using Flask, you can access form data using the `request.form` object. This object contains key-value pairs of all the form fields sent with the request.

   ```python
   form_data = request.form
   ```

   You can then access individual form fields by their name:

   ```python
   username = form_data.get('username')
   password = form_data.get('password')
   ```

2. **Using Django**: If you are using Django, you can access form data using the `request.POST` object. This object contains key-value pairs of all the form fields sent with the request.

   ```python
   form_data = request.POST
   ```

   You can then access individual form fields by their name:

   ```python
   username = form_data.get('username')
   password = form_data.get('password')
   ```

## How to return various HTTP status codes

To return different HTTP status codes in your application, you can use the following steps:

1. **Using Flask**: If you are using Flask, you can return a specific status code by setting the `status` parameter of the `make_response()` function.

   ```python
   from flask import make_response

   response = make_response('OK', 200)
   ```

   In the example above, the response will have a status code of 200 (OK).

2. **Using Django**: If you are using Django, you can return a specific status code by setting the `status` parameter of the `HttpResponse()` function.

   ```python
   from django.http import HttpResponse

   response = HttpResponse('OK', status=200)
   ```

   In the example above, the response will have a status code of 200 (OK).

Remember to import the necessary modules depending on the framework you are using.
