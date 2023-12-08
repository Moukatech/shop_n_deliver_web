<br />
<div align="center">
  <a href="https://github.com/Moukatech/API_Automation">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Web Test Automation</h3>

  <p align="center">
    Test automation framework.
    <br />
  </p>
</div>


## About The Project
The purpose of this project is to showcase how to create a test automation framework using Page Object model(POM) and generate a readable report.

### Built With:

* Python.
* Pytest.
* Allure reporting template.
* Panda - for reading excel data.
* pytest-xdist- to run tests in parallel

## Getting Started

These are the steps to follow when you want to run the project locally.

### Prerequisites

Items required to be installed before you can start running the tests.
These are instructions for a user with a mac device.
* Python
  ```sh
  brew install python
  ```
* Allure
  ```sh
  brew install allure
  ```

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/Moukatech/shop_n_deliver_web
   ```
2. Change directory to the cloned project:
   ```sh
    cd shop_N_deliver_web
   ```
4. Install pipenv to create a virtual environment and activate it:
   ```sh
   pip install pipenv
   pipenv shell 
   ```
4. Install the required packages from the `requirements.txt` file:
   ```sh
   pipenv install -r requirements.txt
   ```
5. To run the tests and generate a report:
   ```sh
   pytest Tests/   
   ```
   -- Currently, I have noticed an error that pytest throws when the allure parameter is passed. "ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]"
   pytest --alluredir=allure_report/ Tests/
   -- is not working for now, still working on a solution for this
7. To be able to view the test results: 
   ```sh
    allure serve allure_report/ 
   ```
8. To run on Different Browsers
   ```sh
     pytest --browser firefox or pytest --browser chrome
   ```
9. To run tests in parallel:
   ```sh
     pytest -n 3
   ```
10. For CI I used github actions for running the tests.
    - check in the actions tab or in the repo .github/workflows for the yml file that runs the tests.

 ## Example of how the final report should look like.
 ![Allure report Screen Shot][Report_Screenshot]
 
 ## Contact
 Lewis Mocha - lewismocha@gmail.com
 
 
 
 
 [Report_Screenshot]: images/Report_Screenshot.png
