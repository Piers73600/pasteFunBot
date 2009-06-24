import copy
import socket

import pkg_resources

from paste.script import templates

var = templates.var
recipe = 'collective.buildbot'

def get_var(vars, name):
    for var in vars:
        if var.name == name:
            return var
        else:
            return ValueError("No such var: %r" % name)

class Template(templates.Template):
    summary = "Projet de test de construction et de montee en charge"
    required_templates = []
    use_cheetah = True
    egg_plugin = [recipe]

    vars = [
        var('project_name', 'Nom du projet'),
	var('port', 'Port d\'ecoute des esclaves', default='9050') 
        ]

class buildbotSlave(Template):
    _template_dir = 'templates/buildbotSlave'
    summary = "Configuration d'un esclave buildbot ainsi que de tests de montee en charge funkload"
    required_templates = []

    vars = copy.deepcopy(Template.vars)
    
    vars.append(
		var('aport', 'Port de l\'application', default='')
		)    

    vars.append(
		var('master_adress', 'Adresse du maitre')
		)
    vars.append(
                var('password', 'Mot de passe de l\'esclave')
                )
    def pre(self, command, output_dir, vars):
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()

    def post(self, *args, **kwargs):
        print "==================================================="
        print "Configuration slave effectuee"
        print "Creez un lien symbolique vers votre python"
        print "dans le dossier bin/ et nomme python-nom_du_projet"
        print "enfin, ajoutez le au PATH du systeme"
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
    vars.append(
		var('vcs_user', 'Username du depot')
		)
    vars.append(
		var('vcs_user_password', 'Mot de passe du depot', should_echo=False)
		)

    def pre(self, command, output_dir, vars):
        vars['recipe'] = recipe
        vars['directory'] = '${buildout:directory}'
        vars['hostname'] = socket.gethostname()
	vars['slaves'] = 'nom_du_slave'
	vars['slaves_pwd'] = 'mot_de_passe_slave'

    def post(self, *args, **kwargs):
        print "==================================================="
        print "Configuration master effectuee"
        print "N'oubliez pas de completer master.cfg (slaves, ...)"
        print "==================================================="  
