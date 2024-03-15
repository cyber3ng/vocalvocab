from setuptools import setup, find_packages


setup(
    name='vocalvocab',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'genanki',
    ],
    entry_points={
        'console_scripts': [
            'vocalvocab=vocalvocab.main:main',
        ],
    },
    include_package_data=True,
)
