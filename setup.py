from setuptools import setup, find_packages

setup(
    name="qhonuskan-votes",
    url='https://github.com/miratcan/qhonuskan-votes',
    license='BSD',
    description="UP/Down voting system, without GenericForeignKey usage.",
    long_description=open('README.markdown', 'r').read(),
    author='Mirat Can Bayrak',
    author_email='miratcanbayrak@gmail.com',
    packages=find_packages(),
    zip_safe=True,
    include_package_data=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

