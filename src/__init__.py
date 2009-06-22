import socket
from paste.script import templates
import pkg_ressources

var = templates.var
recipe = 'collective.buildbot'

def get_var(vars, name):
    for var in vars:
        if var.name == name:
            return var
        else:
            return ValueError("No such var: %r" % name)

class Namespace(templates.Template):
    summary = "Projet de test de construction et de montee en charge"
    required_templates = []
    use_cheetah = True
    egg_plugin = [recipe]

    vars = [
        var('project_name', 'Nom du projet'),
	var('port', 'Port d\'ecoute des esclaves', default='9050') 
        ]

class buildbotSlave(Namespace):
    _template_dir = 'templates/buildbotSlave'
    summary = "Configuration d'un esclave buildbot"
    required_templates = []

    vars = copy.deepcopy(Namespace.vars)
    
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
        print "Configuration esclave terminee"
