try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': "This is all stuff from Tao Pang's computational physics book",
    'author': 'David Plotz',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'chuphay@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['physics'],
    'scripts': [],
    'name': 'physics'
}

setup(**config)
