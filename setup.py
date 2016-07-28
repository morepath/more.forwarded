import io
from setuptools import setup, find_packages

long_description = '\n'.join((
    io.open('README.rst', encoding='utf-8').read(),
    io.open('CHANGES.txt', encoding='utf-8').read()
))

setup(
    name='more.forwarded',
    version='0.3.dev0',
    description="Forwarded header support for Morepath",
    long_description=long_description,
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    keywords='morepath forwarded',
    license="BSD",
    url="https://github.com/morepath/more.forwarded",
    namespace_packages=['more'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 5 - Production/Stable'
    ],
    install_requires=[
        'setuptools',
        'morepath >= 0.15',
    ],
    extras_require=dict(
        test=[
            'pytest >= 2.0',
            'pytest-cov',
            'WebTest >= 2.0.14'
        ],
    ),
)
