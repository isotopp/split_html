from setuptools import setup

setup(
    name='split-html',
    version='1.0',
    py_modules=['split_html'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        split_html=split_html:main
    ''',
)