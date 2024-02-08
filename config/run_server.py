import subprocess
import sys


def run_uvicon():
    uvicorn_command = [
        "py", "-m", "uvicorn", "config.asgi:application",
        "--host", "0.0.0.0", "--port", "8001"
    ]
    subprocess.run(uvicorn_command, check=True)


def run_waitress():
    waitress_command = [
        "py", "-m", "waitress", "--listen=*:8000", "config.wsgi:application"
    ]
    subprocess.run(waitress_command, check=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_servers.py [uvicorn|waitress]")
        sys.exit(1)

    server_type = sys.argv[1].lower()

    if server_type == "asgi":
        run_uvicon()
    elif server_type == "wsgi":
        run_waitress()
    else:
        print("Пропиши:'uvicorn' or 'waitress'.")
        sys.exit(1)

##  python run_servers.py uvicorn


## python run_servers.py waitress
