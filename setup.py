from setuptools import setup, find_packages

setup(
    name="pykage",
    version="0.1",
    author="José Vizcaya",
    author_email="josevizcaya0616@gmail.com",
    description="""A CLI app provided for creating packages in
    environments that does not support that functionality,
    i.e the vast majority of text editors.
    """,
    packages=[
        "pykage_app",
        "pykage_app.packaging"
    ],
    install_requires=[
        "click",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "pykage = pykage_app:main"
        ]
    }
)