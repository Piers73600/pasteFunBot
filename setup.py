from setuptools import setup, find_packages

version = "0.1"

setup(name="pasteFunBot",
    version = version,
    description = "Tool to build and test a complete project",
    long_description = """
	Using buildbot and funkload, allow you to have 
	a feedback of your modifications of a python project with funkload differencial 
	reports and buildbot waterfall
	""",
    classifiers=[],
    keywords = "funkload buildbot funbot pasteFunBot",
    author = "Piers(Pierre-Louis Davallon)",
    author_email = "pl.davallon@gmail.com",
    url = "http://piers73600.github.com/pasteFunBot",
    license = "",
    include_package_data = True,
    zip_safe = True,
    install_requires=[
	'Cheetah',
	'setuptools',
        'PasteScript>=1.3',
    ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    entry_points = """
        [paste.paster_create_template]
        funbot_slave=pasteFunBot.pasteFunBot:buildbotSlave
	funbot_master=pasteFunBot.pasteFunBot:buildbotMaster
	funbot_local=pasteFunBot.pasteFunBot:buildbotLocal
    """
    )
