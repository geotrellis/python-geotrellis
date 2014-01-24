from setuptools import setup, find_packages

setup(
    name='python-geotrellis',
    version='0.1.0',
    author='Azavea',
    author_email='info@azavea.com',
    maintainer='Rob Emanuele',
    maintainer_email='remanuele@azavea.com',
    packages=find_packages(),
    url=['http://github.com/geotrellis/python-geotrellis'],
    scripts=['bin/gtloader'],
    license='LICENSE.txt',
    description='GeoTrellis library for mananging raster data.',
    long_description=open('README.rst').read(),
    install_requires=["gdal >= 1.9.1"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: GIS',
        'Programming Language :: Python :: 2.7'
    ],
)
