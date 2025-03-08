# E-commerce Automation

## Project Overview
This project is an automation framework for testing an **E-commerce application** using **Selenium with Pytest**. It follows the **Page Object Model (POM)** design pattern and integrates with **Docker** for CI/CD execution. The framework also generates test reports using **Allure Reports** and **HTML Reports**.

## Technologies Used
- **Python** (Automation scripting)
- **Selenium** (Web automation)
- **Pytest** (Test framework)
- **Allure Reports** (Test reporting)
- **HTML Reports** (Alternative test reporting)
- **Docker** (Containerized test execution)
- **Page Object Model (POM)** (Design pattern for maintainability)

## Project Structure
```
Ecommerce-Automation/
│-- tests/                 # Test cases
│   ├── test_login.py      # Login test cases
│   ├── test_cart.py       # Cart functionality tests
│   ├── test_checkout.py   # Checkout process tests
│-- pages/                 # Page Object Model (POM) classes
│   ├── login_page.py      # Login page elements & methods
│   ├── cart_page.py       # Cart page elements & methods
│   ├── checkout_page.py   # Checkout page elements & methods
│-- utils/                 # Utility functions (helpers, configurations)
│-- conftest.py            # Pytest configurations & fixtures
│-- requirements.txt       # Project dependencies
│-- docker-compose.yml     # Docker configuration for test execution
│-- pytest.ini             # Pytest configurations
│-- README.md              # Project documentation
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed on your system:
- **Python (>=3.x)**
- **Google Chrome & ChromeDriver** (For Selenium WebDriver execution)
- **Docker** (If running tests in containers)

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running Tests
### Run Tests Locally
```sh
pytest --html=reports/report.html --self-contained-html
```


```

## Reporting
- **HTML Report**: Generates an HTML report of test execution.
- **Allure Report**: Provides an interactive and detailed test execution report.

## CI/CD Integration
The framework is designed to be integrated with **CI/CD pipelines**, enabling automated execution in a **Dockerized** environment.


![image](https://github.com/user-attachments/assets/6fdf7fc2-b32e-46e2-8788-12367850c359)

![image](https://github.com/user-attachments/assets/b4add559-2025-4394-a776-36d587d4a229)

![image](https://github.com/user-attachments/assets/607813a6-6b4d-430c-84d2-163ebd1da662)





