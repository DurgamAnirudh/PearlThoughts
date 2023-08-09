# test.py
import subprocess

def test_hello_world():
    result = subprocess.run(["python", "app.py"], stdout=subprocess.PIPE)
    assert result.stdout.decode("utf-8") == "Hello, World!\n"

if __name__ == "__main__":
    test_hello_world()
