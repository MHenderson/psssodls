from setuptools import setup

setup(name='psssodls',
      version='0.2',
      description='Generate PSSSODLS in Minion 3 format.',
      url='https://gitlab.com/MHenderson1/psssodls-generator',
      author='Matthew Henderson',
      author_email='matthew.james.henderson@gmail.com',
      license='MIT',
      packages=['psssodls'],
      scripts=['bin/psssodls'],
      zip_safe=False)
