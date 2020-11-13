# Example for Poetry + FastAPI + Uvicorn/Gunicorn

## Usage

```powershell
$ poetry run serve              # default Unicorn
$ # poetry run serve uvicorn    # Uvicorn
$ # poetry run serve gunicorn   # Gunicorn
```

```sh
$ poetry run serve  # or poetry run serve uvicorn
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
...
INFO:     127.0.0.1:64319 - "GET / HTTP/1.1" 200 OK
```

```sh
$ poetry run serve gunicorn
[2020-11-13 20:45:11 +0900] [3094] [INFO] Starting gunicorn 20.0.4
[2020-11-13 20:45:11 +0900] [3094] [INFO] Listening at: http://127.0.0.1:8000 (3094)
[2020-11-13 20:45:11 +0900] [3094] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2020-11-13 20:45:11 +0900] [3130] [INFO] Booting worker with pid: 3130
[2020-11-13 20:45:11 +0900] [3130] [INFO] Started server process [3130]
[2020-11-13 20:45:11 +0900] [3130] [INFO] Waiting for application startup.
[2020-11-13 20:45:11 +0900] [3130] [INFO] Application startup complete.
...
127.0.0.1:64456 - "GET / HTTP/1.1" 200
```

## Install

Install pyenv and poetry

```sh
$ pyenv install `cat .python-version`
$ poetry install
```
