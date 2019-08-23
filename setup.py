from setuptools import setup

import versioneer

with open('requirements.txt') as reqs:
    REQUIREMENTS = [reqs.readlines()]

setup(name='sphinx_material',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Material sphinx theme',
      long_description=open('README.rst').read(),
      author='Kevin Sheppard',
      author_email='kevin.k.sheppard@gmail.com',
      url='https://github.com/bashtage/sphinx-material',
      packages=['sphinx_material'],
      include_package_data=True,
      python_requires='>=3.6',
      install_requires=REQUIREMENTS,
      license="MIT",
      classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
      )
      )
