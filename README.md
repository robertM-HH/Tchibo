# Tchibo

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This script uses the unittest module to create a test case for searching for a product on the Tchibo website using Page Object Model (POM).
The test case uses the Selenium webdriver to open the Tchibo website, interact with elements on the website using the HomePage and ProductPage classes,
and asserts that the correct product is displayed on the product page. The test case uses the HtmlTestRunner to generate a report of the test execution.

For the API call tests, Python with Requests and Json is being used to test the API call to the specified endpoint.
	
## Technologies
Project is created with:
* Python version: 3.11
* Selenium version: 4.8.0
* Webdriver-manager version: 3.8.5
* requests: 2.28.2
* jsonpath: 0.82
	
## Setup
To run this project, install it locally using pip:

```
$ cd ../lorem
$ pip install selenium
$ pip install webdriver_manager
$ pip install chromedriver-binary-auto
$ pip install html-testRunner 
$ pip install requests
$ pip install jsonpath
```
