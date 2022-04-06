from setuptools import setup, find_packages

setup(
	name='project1',
	version='1.0',
	author='PAVAN VASANTH KOMMINENI',
	authour_email='pa1vasanth@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)


