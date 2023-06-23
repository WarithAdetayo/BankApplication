># Bank Application
An API for a simple Bank application.

## Available Endpoints

> ### Bank Account Endpoints
| Endpoint      | Method    | Description   |
| :---------     | :---------: | :------        |
| ***api/v1/account/create/*** | _POST_ | To create a bank account|
| ***api/v1/account/view/***  | _GET_ | To view account information (Require Authentication) |
|***api/v1/account/update/*** | _PUT_ | Update basic bank account bio-data information (Require Authentication) |
|***api/v1/account/update/details/*** | _PUT_ | Update bank account information (Require Authentication) |
|***api/v1/account/delete/*** | _DELETE_ | To delete account (Require Authentication)



***

> ### Transaction Endpoints
The following are the to be implemented endpoints
| Endpoint      | Method    | Description   |
| :---------     | :---------: | :------        |
| ***api/v1/transaction/send*** | _POST_ | To send money to another account (Require Authentication) |
| ***api/v1/transaction/receive/*** | _GET_ | To receive from another account (Require Authentication) |
| ***api/v1/transaction/view/\<str:reference_number>/*** | _GET_ | To view a transaction detail by reference_number (Require Authentication) |
| ***api/v1/transaction/list/*** | _GET_ | To list all transactions (Require Authentication) |


## How to Use
- Download and install python (https://www.python.org/downloads/)
- Install Project requirements using pip (**django** and **djangorestframework**)
    - ***pip install -r requirements.txt***

### To run
Navigate to the project's root folder and enter at the terminal:
- ***python3 manage.py runserver*** (unix)
- ***python manage.py runserver*** (windows)

### Testing the API
- Browsable API: You can test the API from the browser by entering the URL endpoint at the browser search area. eg
    - To create an account enter: (http://localhost:8000/api/v1/account/create/)
- Postman: You can use postman or any other client programs to make requests to the API