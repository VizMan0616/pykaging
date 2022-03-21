from setuptools import setup, find_packages

setup(
    name="pykaging",
    version="0.6.6",
    author="José Vizcaya",
    author_email="josevizcaya0616@gmail.com",
    description="""A CLI app provided for creating packages in
    environments that does not support that functionality,
    i.e the vast majority of text editors.
    """,
    url="https://github.com/VizMan0616/pykaging",
    packages=[
        "src",
        "src.packaging"
    ],
    install_requires=[
        "click",
        "colorama"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pykaging = src:main"
        ]
    }
)
