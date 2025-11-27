# UI Test Automation with Python & Playwright

This project automates UI tests for [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) using Python, pytest, and Playwright. It contains report generation using Allure and will later have API tests added.

---

## 📂 Project Structure
PlaywrightUITest/

├── pages/

│ └── yourpage_page.py

├── tests/

│ └── test_yourpage.py

├── conftest.py

├── requirements.txt

├── .gitignore

└── README.md

- `pages/` → Contains all test pages and their fixtures
- `tests/` → Contains all test files
- `conftest.py` → Defines pytest fixtures for browser and page setup
- `requirements.txt` → Python dependencies
- `.gitignore` → Excludes unnecessary or system-specific files from version control
- `README.md` → Documentation
---

## ✅ Prerequisites
- Python ≥ 3.9
- Git
- Playwright CLI (`pip install playwright`)
---

## ⚙️ Installation
### 1. Clone the Repository
```bash
git clone https://github.com/MAnitsu/PlaywrightUITest.git
cd PlaywrightUITest
```

### 2. Create a Virtual Environment
The virtual environment is not included in the repository. Each user should generate it locally depending on their OS.

```bash
# Windows:
python -m venv venv
venv\Scripts\activate # activates environment
deactivate # deactivates environment after running tests

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install
```
### 💡 Notes
The venv/ folder is excluded via .gitignore to keep the repository clean and OS-independent.

Regenerating the virtual environment ensures consistency across contributors without committing system-specific binaries.

## 🧪 Running Tests
Run all tests:
```bash
pytest
```
Run a specific test file:
```bash
pytest tests/test_login.py
```
Run tests with detailed output:
```bash
pytest -v
```
Run tests and generate an easy to read report
```bash
pip install pytest-html
pytest --html=report.html --self-contained-html # to run the tests and generate the report
# Run tests with Allure Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results

```

## 📄 How to Create New Tests
### 1. Create a new file in pages/ to import the page fixtures:
```python
class YourPage:
    def __init__(self, page: Page): # in the constructor all the locators needed must be assigned
        self.page = page
        self.yourlocator = page.locator("#yourlocatorhere")

    def navigate(self): # navigate action is mandatory to be able to load the page
        self.page.goto("https://yourpagehere.test")

    def action(self): # define any action you need to be performed on locators, in this example checking a checkbox
        action = self.yourlocator.check()

    def check(self) -> bool: # define a check function that returns a boolean value to be able to check if an action was performed or not
        return self.yourlocator.is_checked()
```
### 2. Create a new file in tests/ where the tests will be written using the methods from the pages, making them easy to read, like scripts:
```bash
def test_yourpage(page):
    yourpage_page = YourPage(page)
    yourpage_page.navigate() # loads the page
    
    # perform action
    yourpage_page.action()

    # check that your action was performed
    assert yourpage_page.check() is True # if the action was performed, the test will pass, else the test will fail
```

### 3. Use Playwright commands:
- page.goto(url)
- page.fill(selector, text)
- page.click(selector)
- page.locator(selector).is_visible()
- page.locator(selector).inner_text()

## 🔎 Playwright Locator Tips
Examples:
```python
page.locator("#username")
page.locator(".button")
page.locator("button[type='submit']")
```

## 📂 Managing Test Data (will expand on this later with a script that creates test data)
For file upload tests, create a dummy file:
```bash
echo "Hello World" > testfile.txt
```

## 🚀 Ways to Expand This Project

### Done
✅ Implement the Page Object Model (POM)

✅ Generate HTML test reports (e.g. pytest-html)

### To do
✅ Use pytest parametrise to test multiple inputs

✅ Add API tests

✅ Integrate with GitHub Actions for Continuous Integration

✅ Run tests in headless mode for speed

✅ Test on multiple browsers (Chromium, Firefox, WebKit)

## 📝 Useful Commands
Run Playwright Codegen (record actions):
```bash
playwright codegen https://the-internet.herokuapp.com/
```
Update requirements.txt:
```bash
pip freeze > requirements.txt
```
Deactivate virtual environment:
```bash
deactivate
```

## 👨‍💻 Author
MAnitsu

GitHub Profile: https://github.com/MAnitsu
