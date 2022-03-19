from setuptools import setup


setup(
    name="pykage",
    version="0.1",
    packages=[
        "pykage-app"
    ],
    py_modules=[],
    install_requires=[
        "click",
        "colorama"
    ],
    entry_points={
        "console_scripts": []
    }
)