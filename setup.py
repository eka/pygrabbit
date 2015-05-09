import io
import os
from setuptools import setup

def get_path(*args):
    return os.path.join(os.path.dirname(__file__), *args)

def get_requirements(filename='requirements.txt'):
    with io.open(get_path(filename), 'rt', encoding='utf8') as fd:
        data = fd.read()
        lines = map(lambda s: s.strip(), data.splitlines())
    return [l for l in lines if l and not l.startswith('#')]

setup(name='pygrabbit',
      version='0.1',
      description='PyGrabbit is a simple URL scraper based on the Ruby Grabbit',
      long_description="""PyGrabbit is a simple URL scraper.
      It returns the best image (or several images) that represents the content
      on a given web page. Grabbit also returns a title, and a description for the page.
      It was inspired by the Ruby version https://github.com/rlarcombe/grabbit""",
      url='http://github.com/eka/pygrabbit',
      author='Esteban (Eka) Feldman',
      author_email='esteban.feldman@gmail.com',
      license='MIT',
      packages=['pygrabbit'],
      zip_safe=False,
      install_requires=get_requirements()
      )