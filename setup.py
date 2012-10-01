
# encodig: utf-8

from setuptools import setup


setup(name='mstranschain',
      version='0.0',
      description="Utility for chaining translations between multiple languages",
      author='Ymat',
      author_email='drowse314@gmail.com',
      url='',
      py_modules=['mstranschain',],
      requires=['ssl', 'microsofttranslator'],
      provides=['mstranschain'],
      package_data=['README.md', 'LICENCE'],
      licence='MIT',
      )
