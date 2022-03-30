import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Buyers Scoring",
    version="0.0.1",
    author="Diego Sendra",
    author_email="diego@wabel.com",
    description="Buyers Scoring updates the score of a contact. It also assigns a quality score for a contact.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['BuyersScoringList', 'BuyersScoringUpdate'],
    package_dir={'BuyersScoringList': 'BuyersScoringList',
                 'BuyersScoringUpdate': 'BuyersScoringUpdate'},
    package_data={'BuyersScoringList': ['data/*.sql', 'conf.ini'],
                  'BuyersScoringUpdate': ['data/*.sql', 'conf.ini']},
    url="https://github.com/needl-app/Timeline_Dashboard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "python-dotenv",
        "pymysql",
        "sqlalchemy",
	"configparser",
	"datetime",
	"pandas",
	"array",
	"pathlib"
	"exception"
    ]
)
