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


version = __import__('pygrabbit').__version__

setup(name='pygrabbit',
      version=version,
      description='PyGrabbit is a simple URL scraper that will try to get the best image given the web page.',
      long_description="""From the entrails of 'Skynet' comes PyGrabbit, a very clever bastard that will not stop at anything to fulfill its purpose.

PyGrabbit is a simple URL scrapper inspired by the Ruby Grabbit https://github.com/rlarcombe/grabbit. It will try to return the best image(s) that represent the content on a given web page or not.""",
      url='http://github.com/eka/pygrabbit',
      author='Esteban (Eka) Feldman',
      author_email='esteban.feldman@gmail.com',
      license='MIT',
      packages=['pygrabbit'],
      zip_safe=False,
      install_requires=get_requirements()
      )
