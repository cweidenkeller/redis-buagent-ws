from setuptools import setup, find_packages


setup(name='redis-buagent-ws',
      version='0.0.1',
      url='https://github.com/cweidenkeller/redis-buagent-ws',
      author='Conrad Weidenkeller',
      author_email='conrad@weidenkeller.com',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['redis-buagent-ws = redis_buagent_ws.run:run']
      })
