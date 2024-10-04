## Project Title: Data Collection Web Application API

## Description: This is a REST API for a Data Collection Web Application built using Django and Django Rest Framework (DRF). The API handles the collection of customer details in a field by registered users (staffs), with details such as 
 * Customer Name,
 * Location Tracking, 
 * Payment Details (Amount Paid), and 
 * Operational Status


## Table of Contents
- [In-Scope]
- [Setup]
- [API Endpoints]


* In-Scope: 
     * Admin can access all customer inputted
     * Admins can alter and make changes to the status of the customer from "Not Done" to "Done"


* Setup: To access and interact with the project with POSTMAN follow this steps using the terminal
	1. Create a virtual Enviroment: "python -m venv .venv"
	2. Activate the virtual enviroment: ". venv/scripts/activate"
	3. Run the server: python manage.py run server

* API Endpoints:
 	AUTHENTICATION:
		POST /auth/registration
		Content-Type: application/json
		Fields: username, first_name, last_name, email, password	
		Test Samples:
			{
			    "username": "Pius",
			    "first_name": "Daniel",
			    "last_name": "Faruna",
			    "email": "test@gmail.com",
			    "password": "1234"
			}


		POST /auth/login
		Content-Type: application/json
		Fields: email, password
		Test Samples:
			{
			    "email": "test@gmail.com",
			    "password": "1234"
			}
	
	CUSTOMER CREATION (Only Autenticated Users can access this endpoint):
		POST /api/customers/
          Authorization: Access_Token
          Field: customer_name, location, amount_paid, volume_dispensed, status
          Content-Type: application/json
          {
               "customer_name": "Egbetokun Timilehin",
               "location": "Lagos",
               "amount_paid": 32,
               "volume_dispensed": 4,
               "status": "Not Done"
          }