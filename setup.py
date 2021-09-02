from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="free-proxy-list",
    version="0.0.1",
    author="Sohail Ahmed",
    author_email="meetsohail360@gmail.com",
    description="This package is to get free proxy ips and port number for scraping and for testing on proxy.",
    url="https://github.com/meetsohail/proxy-list",
    keywords='proxy, server, scraping, request, python, selenium',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)
