import os.path
from setuptools import setup

pkg_name = 'qhonuskan-votes'
pkg_version = __import__(pkg_name.replace('-', '_')).__version__

# get requires from requirements/global.txt file.
requires_file_name = os.path.join(
    os.path.dirname(__file__), 'requirements', 'global.txt')
with file(requires_file_name) as install_requires:
    install_requires = map(lambda x: x.strip(), install_requires.readlines())

setup(
    name=pkg_name,
    version=pkg_version,
    url='https://github.com/linkfloyd/qhonuskan-votes',
    license='GPL',
    description="Easy to use reddit like voting system for django models.",
    long_description=open('README.rst', 'r').read(),
    author='Mirat Can Bayrak',
    author_email='miratcanbayrak@gmail.com',
    packages=[
        'qhonuskan_votes',
        'qhonuskan_votes.templatetags'
    ],
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
