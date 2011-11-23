from setuptools import setup, find_packages

setup(
    name="django-votes",
    url='https://github.com/citylive/django-votes',
    license='BSD',
    description="Voting system for various things",
    long_description=open('README.markdown', 'r').read(),
    author='Maarten Timmerman, City Live nv',
    packages=find_packages('src'),
    package_data={'django_votes': [
                'static/*/*/*.js',
                'static/*/*/*.css',
                'static/*/*/*.png',
                'templates/*/*.html'
                ], },
    zip_safe=False, # Don't create egg files, Django cannot find templates in egg files.
    include_package_data=True,
    package_dir={'': 'src'},
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)

