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
    summary = "Projet de test de construction et de montee en charge"
    required_templates = []
    use_cheetah = True
    egg_plugin = [recipe]

    vars = [
        var('project_name', 'Nom du projet'),
	var('port', 'Port d\'ecoute des esclaves', default='9050') 
        ]

class buildbotLocal(templates.Template):
    summary = "Projet de test de construction et de montee en charge en local"
    required_templates = []
    use_cheetah = True
    _template_dir = 'templates/buildbotLocal'
    egg_plugin = [recipe]

    vars = [
	var('vcs', 'Utilitaire de versionnement utilise', default='svn'),
	var('vcs_url', 'Url du depot'),
        var('email', 'Adresse de reception des rapports')
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
        print "Configuration de l'application en local effectuee"
	print "Verifiez les fichiers de configuration"
        print "Pensez a lire les LISEZ-MOI"
        print "==================================================="

class buildbotSlave(Template):
    _template_dir = 'templates/buildbotSlave'
    summary = "Configuration d'un esclave buildbot ainsi que de tests de montee en charge funkload"
    required_templates = []

    vars = copy.deepcopy(Template.vars)
    
    vars.append(
		var('master_adress', 'Adresse du maitre')
		)
    vars.append(
		var('aport', 'Port de l\'application testee', default='')
		)
    vars.append(
		var('pport', 'Port utilise pour acceder au buildbot et aux rapports', default='8000')
		)    
    vars.append(
		var('email', 'Adresse de reception des rapports')
		)    

    def pre(self, command, output_dir, vars):
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()
	vars['password'] = ''.join([random.choice(string.ascii_letters) for i in range(8)])
        vars['pythonpath'] = os.path.dirname(sys.executable)
	
    
    def post(self, *args, **kwargs):
	print "==================================================="
        print "Configuration slave effectuee"
	print "Pensez a lire les LISEZ-MOI"
        print "==================================================="

class buildbotMaster(Template):
    _template_dir = 'templates/buildbotMaster'
    summary = "Configuration d'un maitre buildbot"
    required_templates = []

    vars = copy.deepcopy(Template.vars)
	
    vars.append(
		var('url', 'Url du projet', default='127.0.0.1'),		
                )
    vars.append(
		var('wport', 'Port utilise pour l\'interface web', default='9080')
		)
    vars.append(
		var('vcs', 'Utilitaire de versionnement utilise', default='svn')
		)
    vars.append(
		var('vcs_url', 'Url du depot')
		)

    def pre(self, command, output_dir, vars):
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()
	vars['slaves'] = 'nom_du_slave'
	vars['slaves_pwd'] = 'mot_de_passe_slave'
	vars['vcs_user'] = ''
	vars['vcs_user_password'] = ''

    def post(self, *args, **kwargs):
        print "=================================================================="
        print "Configuration master effectuee"
        print "N'oubliez pas de completer master.cfg (slaves, buildsequence, ...)"
	print "Pensez a lire les LISEZ-MOI"
	print "=================================================================="  
