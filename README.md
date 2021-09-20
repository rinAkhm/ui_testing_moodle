[![Build Status](https://app.travis-ci.com/rinAkhm/ui_testing_moodle.svg?branch=master)](https://app.travis-ci.com/rinAkhm/ui_testing_moodle)
# Lms Moodle testing 
UI python tests with https://qacoursemoodle.innopolis.university

This is project used for training test UI. Just used Selenium

Purposes:
1. write autotests for authorization
2. write autotests changing profile data
3. write autotests for creating a course.

### How to Quickstart
1. Use python 3.9
2. Create virtual environments with using the command:
```
python -m venv venv
```
3. Clone repository on your machine
```
git clone https://github.com/rinAkhm/ui_testing_moodle.git
```
4. Before run beginning you need install packets. Run in terminal
```
pip install -r requirements.txt
```
5. For Run tests need to write command in terminal:
```
pytest -v
```
To install and configure allure, you can help to [link](https://www.youtube.com/watch?v=6qASwPL86MM)

6. For report used Allure need to write command in terminal:
```
pytest --alluredir=report
allure serve report
```
