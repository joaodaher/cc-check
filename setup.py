from distutils.core import setup

from cc_check import __version__

setup(name="cc-check",
      version=__version__,
      description="A library that checks cardholder's name similarity to user's name",
      author="Joao Daher Neto",
      author_email='joao.daher.neto@gmail.com',
      url="https://github.com/joaodaher/cc-check",
      license="MIT",
      keywords="createsend campaign monitor email",
      packages=['cc_check'],
      )
