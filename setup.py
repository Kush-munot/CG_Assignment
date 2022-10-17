from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py-imagizer',
    version='0.0.1',
    description='It is one stop app that is used for Image Processing and Image Editing.The app has ability to change any image into its dense pencil sketches, colour pencil sketch, colour paints, cartoon image, water colour paints effect, etc. We have use Open CV and Numpy as dependencies that run the Package and you and freely contribute new pieces of code on Github',
    author= 'Kush Munot',
    url = 'https://github.com/Kush-munot/CG_Assignment',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['image processing', 'numpy', 'opencv', 'kush munot', 'py-imagizer', 'imagizer', 'image filters', 'filters', 'image to sketch', 'image to cartoon', 'image to oil paint', 'image to water color', 'blur image'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10.0',
    py_modules=['py-imagizer'],
    package_dir={'':'src'},
    install_requires = [
        'opencv-python',
        'numpy',
        'opencv-contrib-python'
    ]
)