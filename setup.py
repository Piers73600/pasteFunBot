from setuptools import setup, find_packages

version = "0.1"

setup(name="pasteFunBot",
    version = version,
    description = "construction et test de monte en charge",
    long_description = "rien",
    classifiers=[],
    keywords = "",
    author = "Piers",
    author_email = "",
    url = "stpda@cgit.makina-corpus.net:~/git/pasteFunBot.git",
    license = "GNU",
    include_package_data = True,
    zip_safe = True,
    install_requires=[
	'Cheetah',
	'setuptools',
        'PasteScript>=1.3',
	'python-dev',
	'python-xml',
	'python-setuptools',
	'funkload' 
    ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    entry_points = """
        [paste.paster_create_template]
        funbot_slave=pasteFunBot.pasteFunBot:buildbotSlave

    """
    )
