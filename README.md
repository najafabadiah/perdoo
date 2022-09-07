# perdoo

# Installing requirements

Some Python requirements must be satisfied:

    $ pip install -r requirements.txt


# URLs

> POST
``/user/register``

You can create a new user for the given parameters:
- email
- username
- password

And it return a token which you can use for authentication. For example:
```
{
    "token": "f5cb35e042a81f82403e78f29b1ed5f2e39844c6"
}
```


> POST
``/user/login``

You can login with the given parameters:
- username
- password

And it return a token which you can use for authentication. For example:
```
{
    "token": "f5cb35e042a81f82403e78f29b1ed5f2e39844c6"
}
```

For clients to authenticate, the token key should be included in the `Authorization` HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```


> GET
``/schedulerApp/request``

Get list of all request:
```
[
    {
        "id": 5,
        "title": "dlroW olleH",
        "scheduledDateTime": "2022-09-07T13:33:00+02:00",
        "status": "completed"
    },
    {
        "id": 6,
        "title": "Hello World End",
        "scheduledDateTime": "2022-09-07T14:30:00+02:00",
        "status": "pending"
    }
]
```


> POST
``/schedulerApp/request``

Create a new request and schedule it to run in the future. The following parameters must pass alongside the request:
- title
- scheduledDateTime `format: yyyy-mm-dd HH:MM:SS`

