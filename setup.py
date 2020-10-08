from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='gupshup_python_api_client',
    version='0.7.0',

    description='Python client for Gupshup Public API',
    long_description=readme(),
    long_description_content_type='text/markdown',

    url='https://github.com/sendbee/gupshup-python-api-client',
    licence='MIT',

    author='Sendbee ltd',
    author_email='info@sendbee.io',

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='gupshup api python',

    packages=find_packages(),
    install_requires=[
        'click>=7.0',
        'requests>=2.20.0',
        'dumpit>=0.5.0',
        'aenum>=2.1.2',
        'ujson==2.0.1',
    ],

    project_urls={
        'Source': 'https://github.com/sendbee/gupshup-python-api-client',
    },
)
