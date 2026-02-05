# Python Automation with Selenium and Appium

This project is designed for web and mobile automation using Selenium and Appium.

## Project Structure

```
python-automation/
│
├── tests/
│   ├── test_web_login.py
│   └── test_mobile_login.py
│
├── pages/
│   ├── web_login_page.py
│   └── mobile_login_page.py
│
├── utils/
│   └── driver_factory.py
│
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start Appium server for mobile automation:
   ```
   appium
   ```

3. Run tests using your preferred test runner (e.g., pytest).