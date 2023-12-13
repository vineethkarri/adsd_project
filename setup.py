# setup.py

from setuptools import setup

setup(
    name='your_app_name',
    version='1.0',
    packages=['your_app_name'],
    install_requires=[
        'bottle',
        'sqlite3',
    ],
    entry_points={
        'console_scripts': [
            'your_app_name = your_app_name.application:main',
        ],
    },
)
