from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Robin Norwood',
    author_email='robin@acloud.guru',
    desciption='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/python-basics-101/automating-aws-with-python.git',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''

)
