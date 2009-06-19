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
    url = "git://stpda@cgit.makina-corpus.net/home/users/stpda/pasteFunload.git",
    license = "GNU",
    packages = ,
    include_package_data = True,
    zip_safe = True,
    install_requires=[
        'PasteScript>=1.3'
    ],
    entry_point = """
        [paste.paster_create_template]
        funbot=pasteFunBot.paster:Namespace
    """
    
