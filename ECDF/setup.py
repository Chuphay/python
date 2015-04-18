try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Computes the empirical cumulative distribution function of the average test score of students who attended a particular school, which is specified as a parameter to the program.',
    'author': 'David Plotz',
    'url': 'https://github.com/Chuphay/python/tree/master/ECDF',
    'download_url': 'https://github.com/Chuphay/python/tree/master/ECDF.git',
    'author_email': 'chuphay@gmail.com',
    'version': '0.1',
    'install_requires': ['scipy','numpy'],
    'packages': ['ecdf'],
    'scripts': [],
    'name': 'empirical cdf'
}

setup(**config)
