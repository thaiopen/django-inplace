from setuptools import setup, find_packages
import os
import cms


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Scientific/Engineering :: GIS',
]

setup(
    author="Eric Brelsford",
    author_email="ebrelsford@gmail.com",
    name='django-places',
    version=cms.__version__,
    description='A set of helpers for writing place-based applications with GeoDjango.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/ebrelsford/django-inplace',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.3.1',
        'geojson>=1.0.1',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,
)
