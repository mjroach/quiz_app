from setuptools import setup

install_requires = [
    'django>1.9',
    'django-formtools',
]


setup(
    name='quiz app',
    version='0.1',
    author='Marshall Roach',
    author_email='marshall.roach@gmail.com',
    description='A simple setup for a django app that demonstrates my knowledge. ',
    install_requires=install_requires
)