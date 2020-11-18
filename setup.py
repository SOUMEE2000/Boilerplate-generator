from setuptools import setup

setup(
   name='Manage',
   version='1.00',
   py_modules=['manage'],
   install_requires=[
    'Click','Pandas'
    ],
    entry_points='''
        [console_scripts]
        manage=manage:cli
    ''',
)
