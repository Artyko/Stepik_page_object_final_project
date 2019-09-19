# Stepik selenium
This is the final project for the course: [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575)

The project implemented autotests for [Training site](http://selenium1py.pythonanywhere.com/) with using a pattern Page Object Model 


### Requirements

```
pytest==5.1.1
selenium==3.14.0
```

## Running the tests
To run the basic tests for a review:
```
pytest -v --tb=line --language=en -m need_review
```

### More tests

The project also presents autotests two different pages for guests and authorized users:

```
pytest --tb=line test_main_page.py
pytest --tb=line test_product_page.py
pytest --tb=line -m register_user
pytest --tb=line -m login_guest
```

### Thanks

<img src="https://media.giphy.com/media/heIX5HfWgEYlW/giphy.gif">

