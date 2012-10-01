
# encodig: utf-8

from setuptools import setup


setup(name='mstranschain',
      version='0.0',
      description="Utility for chaining translations between multiple languages",
      author='Ymat',
      author_email='drowse314@gmail.com',
      url='',
      package_dir={'mstranschain': '.'},
      packages=['mstranschain',],
      requires=['ssl', 'microsofttranslator'],
      provides=['mstranschain'],
      # package_data={'mstranschain': ['README.md', 'LICENCE']},
      include_package_data = True,
      license='MIT',
      )
