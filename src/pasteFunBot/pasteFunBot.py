import copy
import socket
import random
import pkg_resources
import string
import os, sys
from paste.script import templates

var = templates.var
recipe = 'collective.buildbot'

class Template(templates.Template):
    summary = "Build and workload test project"
    required_templates = []
    use_cheetah = True
    egg_plugin = [recipe]

    vars = [
        var('project_name', 'Project name'),
	var('port', 'Slaves listening port', default='9050') 
        ]

class buildbotLocal(templates.Template):
    summary = "Build and workload local test project"
    required_templates = []
    use_cheetah = True
    _template_dir = 'templates/buildbotLocal'
    egg_plugin = [recipe]

    vars = [
	var('vcs', 'VCS used', default='svn'),
	var('vcs_url', 'Repoze URL'),
        var('email', 'Reports delivery adress')
	]

    def pre(self, command, output_dir, vars):
	vars['vcs_user'] = ''
	vars['vcs_user_password'] = ''
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()                               
        vars['password'] = ''.join([random.choice(string.ascii_letters) for i in range(8)]) 
        vars['pythonpath'] = os.path.dirname(sys.executable) 
	vars['aport'] = '8080'	
	vars['pport'] = '8000'

    def post(self, *args, **kwargs):
        print "==================================================="
        print "Local application settings complete"
	print "Please check the conf files"
        print "We advice you to read the README"
        print "==================================================="

class buildbotSlave(Template):
    _template_dir = 'templates/buildbotSlave'
    summary = "FunBot slave configuration"
    required_templates = []

    vars = copy.deepcopy(Template.vars)
    
    vars.append(
		var('master_adress', 'Master adress')
		)
    vars.append(
		var('aport', 'Application port', default='')
		)
    vars.append(
		var('pport', 'Reports port', default='8000')
		)    
    vars.append(
		var('email', 'Reports delivery adress', default='me@somedomain.com')
		)    

    def pre(self, command, output_dir, vars):
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()
	vars['password'] = ''.join([random.choice(string.ascii_letters) for i in range(8)])
        vars['pythonpath'] = os.path.dirname(sys.executable)
	
    
    def post(self, *args, **kwargs):
	print "==================================================="
        print "Slave settings complete"
	print "We advice you to read the README"
        print "==================================================="

class buildbotMaster(Template):
    _template_dir = 'templates/buildbotMaster'
    summary = "FunBot master configuration"
    required_templates = []

    vars = copy.deepcopy(Template.vars)
	
    vars.append(
		var('url', 'Project URL', default='127.0.0.1'),		
                )
    vars.append(
		var('wport', 'Web interface port', default='9080')
		)
    vars.append(
		var('vcs', 'VCS used', default='svn')
		)
    vars.append(
		var('vcs_url', 'Repoze URL')
		)

    def pre(self, command, output_dir, vars):
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()
	vars['slaves'] = 'slavename'
	vars['slaves_pwd'] = 'slavepassword'
	vars['vcs_user'] = ''
	vars['vcs_user_password'] = ''

    def post(self, *args, **kwargs):
        print "=================================================================="
	print "Master settings complete"
        print "Don't forget to complete the master.cfg (slaves, buildsequence,...)"
	print "We advice you to read the README"
	print "=================================================================="  
