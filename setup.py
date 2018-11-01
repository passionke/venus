from setuptools import setup, find_packages
import os
import sys

platform = sys.platform

platform_file = ''

if 'linux' in platform:
    platform_file = 'venus/os_tools/linux.py' 
elif 'win32' in platform:
    platform_file = 'venus/os_tools/windows.py' 
elif 'darwin' in platform:
    platform_file = 'venus/os_tools/darwin.py' 


setup(
    name='venus',
    version='0.0.1',
    author="Alfredo Sequeida",
    description="A cross platform tool for setting a random wallpaper image from unsplash.com",
    license="MIT",
    packages=['venus'],
    scripts=[platform_file],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={"console_scripts": ["venus = venus.venus:main"]},
)
