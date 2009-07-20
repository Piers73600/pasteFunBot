==============================================================================
				FunBot
==============================================================================

******************************Description*************************************

The funbot paster allow you to create a project which contains the 
construction of an application and moreover workload tests thanks to the
funkload tool.

*****************************Requirements*************************************

For the master:
---------------

Nothing


For the slave:
--------------

You'll have to install:
	- gnuplot (via apt-get for example), to be able to generate reports
	- an apache server, to display those reports and allow you to see it from the outside

****************************Why such a paster ?*******************************

The reason of the creation of this paster, was the necessity of running 
workload tests every day and compare the results of modifications on the
application.
The advantage to use buildbot is to verify if the application is still 
building before running the tests.
And to finish, receive the differencial report by mail to have a glimpse
about the modifications.

*********************************Use******************************************

First of all, once you got FunBot, you should verify if the installation succeeded.
To do this, just type in the following command:

paster create --list-templates

And you should see something like this:

funbot_local:	Set-up a complete local version of Funbot
funbot_master:	Set-up a master for FunBot
funbot_slave:	Set-up a slave for FunBot

As you can see, FunBot is well-installed !
Now, the next step is tu use it:

paster create -t funbot_local
or
paster create -t funbot_master
or
paster create -t funbot_slave

You'll have to answer to different questions about the project. At the end,
the general configuration of the project will be done.
However, there's still some actions to perform.

****************************Configuration*************************************

Note:
- Don't forget to edit the both build-sequence and test-sequence in the 
master.cfg file to fit to your application.
- If you want to use a specific virtual environment, at the moment of
typing-in "python bootstrap.py" and "./bin/buildout" please activate the one
you wish to use.


If you have created a local FunBot:
-----------------------------------

Simply take a look to the configuration files (master.cfg and slave.cfg) and
use the following commands:

python bootstrap.py
./bin/buildout

From this time, your local FunBot is well-configured, now just launch the
master and the slave:

./bin/master [start | restart | stop]
./bin/hostname [start | restart | stop]

In order to eased the access to the reports realized by FunBot, you sould
use the following command which will allow you to access it with an adress    
such as http://localhost:8000/reports/report_name/ :                          

paster serve reports.ini &  


If you have created a master:
-----------------------------

Firstly, edit the master.cfg file and fill in the slave(s) name and password(s).
Secondly, in the same file, as said in the note, you can specify the commands
to run by the slaves of the project.
More precisely, for the test-sequence, we decided to use makefiles to write
the tests which are located in the sub-repositories of funkload/.
You can find examples of makefiles in the basic repositories.
We advice you to use the make command in the test-sequence.

Once the configuration is realized, type in the following commands:

python bootstrap.py
./bin/buildout

From this time, your master is well-configured, therefore you can launch it:

./bin/master [start | restart | stop]

If you have created a slave:
----------------------------

First of all, we advice you to take a look to the test files contains in the 
funkload repository for you to be able to come to grips with this tool.
A readme explaining the use of funkload is available in that repository.

Once the configuration is realized, type in the following commands:

python bootstrap.py
./bin/buildout

From this time, your slave is well-configured, therefore you can launch it:

./bin/slavename [start | restart | stop]

In order to eased the access to the reports realized by FunBot, you sould
use the following command which will allow you to access it with an adress
such as http://localhost:8000/reports/report_name/ :

paster serve reports.ini &

Finally, just verify the execution rights of the make_reports.sh file.
If the righ "x" is not available for the users, just change it.


