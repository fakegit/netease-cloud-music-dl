# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='netease-cloud-music-dl',
    version='0.3.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.17.3',
        'pycryptodomex',
        'mutagen>=1.38.0',
        'Pillow>=12.0.0',
    ],

    entry_points={
        'console_scripts': [
            'ncm = ncm.start:main',
        ]
    },

    license='MIT',
    author='codezjx',
    author_email='code.zjx@gmail.com',
    url='https://github.com/codezjx/netease-cloud-music-dl',
    description='Netease cloud music song downloader, with full ID3 metadata!',
    keywords=['ncm', 'netease', 'cloud-music', 'downloader'],
)