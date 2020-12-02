from setuptools import setup, find_namespace_packages
setup(
    name="HelloWorld",
    version="0.1",

    packages=find_namespace_packages(),
    # packages=['greeter'],

    entry_points={
        "console_scripts": [
            "say-hello = greeter.hello:say_hello"
        ]
    }

    # scripts=['say_hello.py']
)
