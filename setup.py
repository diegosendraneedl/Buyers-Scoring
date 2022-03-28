import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libname",
    version="0.0.1",
    author="Alexandre Guillemine",
    author_email="alexandre.guillemine@needl.co",
    description="A package to compute discrepancies every day'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['libname.name_of_your_service_1', 'libname.name_of_your_service_2'],
    package_dir={'libname.name_of_your_service_1': 'libname/name_of_your_service_1',
                 'libname.name_of_your_service_2': 'libname/name_of_your_service_2'},
    package_data={'libname.name_of_your_service_1': ['data/*.sql', 'conf.ini'],
                  'libname.name_of_your_service_2': ['data/*.sql', 'conf.ini']},
    url="https://github.com/needl-app/Timeline_Dashboard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "python-dotenv",
        "pymysql",
        "sqlalchemy"
    ]
)
