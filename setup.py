from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A hardware check package'
LONG_DESCRIPTION = 'A package that makes it easy to find out if your pc runs properly'

setup(
    name="hardcheck",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Diac Adrian",
    author_email="diacadi@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=['psutil','shutil'],
    keywords=['hardware','pyhton','usage','cpu','disk'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
