from setuptools import setup

setup(
    name='brename',
    version='1.0.0',
    summary="Batch Rename Files",
    home_page="https://github.com/anaclumos/tools-bulk-rename-files/",
    author="anaclumos",
    license="MIT",
    description="Batch Rename Files",
    entry_points={
        'console_scripts': [
            'brename=brename:run'
        ]
    },

)
