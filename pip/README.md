# pip

`pip` is used in EKG to install Python packages from the Python Package Index (PyPI).

## Usage

To use `pip` in your EKG file, add the following line:

```ekg
get pip
```

Followed by the package name you want to install:

```ekg
pip package_name
```

## Example

Here is an example of how to use `pip` to install the Flask package:

```ekg
get pip
pip flask
```

This will install the Flask package, making it available for use in your EKG script.