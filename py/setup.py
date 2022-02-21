# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Initial setup
"""

from setuptools import setup, find_packages

p={}

with open("data_mining/__init__.py", 'r') as f:
    exec(f.read(), p)
    V = p['__version__']
    
setup(
        name="twitter_data_mining",
        version=V,
        description="Twitter data mining",
        author="Anjali",
        author_email="anjali94venu@gmail.com",
        license="proprietary",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[],
        zip_safe=False
)
