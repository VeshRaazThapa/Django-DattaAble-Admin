from setuptools import setup, find_packages

import app


setup(
    name='monastery_dashboard_app',
    version='0.01',
    description='',
    author='VeshRaj',
    url='https://github.com/VeshRaazThapa/monastery_project_dashboard.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
