# Create Project and Manage Dependencies with Poetry

[Poetry Installation in Windows](https://gist.github.com/Isfhan/b8b104c8095d8475eb377230300de9b0)
[Explore it!](https://realpython.com/dependency-management-python-poetry/)

## 1. Check Version

```bash
python --version
# AND
poetry --version
```

## 2. Create Project

```bash
poetry new myproject
```

## 3. Change Directory

```bash
cd myProject
```

## 4. Create Virtual Environment

```bash
poetry run python --version
```

## 5. Install Dependencies

```bash
poetry add requests
# AND
poetry add pytest
```

After installing, the dependencies will show in `pyproject.toml` file:

![Ss](/public/pic-2.jpg)

## 6. Run 'Hello World'

* Create `.py` file, like:

![Ss](/public/pic-1.jpg)

* Create Function in `main.py`. [View code](/myProject/myproject/main.py)

* Run `poetry run python ./myProject/main.py` in terminal and the result will show.

![Ss](/public/pic-3.jpg)

## 7. Testing

* Make a file (name starts with `test_`) in  `tests` folder:

![Ss](/public/pic-4.jpg)

* Write test functions along with importing `main.py` file. [View code](/myProject/tests/test_myTest.py)

* Run `poetry run pytest` / `poetry run pytest -v` (ensure you've run `poetry add pytest` before)

![Ss](/public/pic-5.jpg)

## Build & Publish

* You first have to create an account and log-in into [PYPI.org](https://pypi.org/)

* Then run these commands to publish:

```bash
poetry build
# AND
poetry publish
```