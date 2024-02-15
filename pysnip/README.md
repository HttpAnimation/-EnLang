# pysnip

`pysnip` is used in EKG to execute Python code snippets.

## Usage

To use `pysnip` in your EKG file, add the following markers to delimit the Python code snippet:

```ekg
pysnip -//
 print("Python code snippet here")
//-//
```

Within the markers, you can write any valid Python code that you want to execute.

## Example

Here is an example of how to use `pysnip` to define a Flask application in EKG:

```ekg
get pysnip
pysnip -//
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, world!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
//-//
```

This will execute the Python code snippet defined between the `pysnip` markers, in this case, defining a Flask application with a single route that returns "Hello, world!" as an HTML heading.