================================================================================
                                  Buildbot
           Outil de construction d'application maître/esclave
================================================================================

******************************Pré-recquis***************************************

Pour installer buildbot, vous faudra avoir installé sur votre système le paquet python-dev 
correspondant à votre version de python (ex: python2.4-dev)

****************************Démarage rapide*************************************

Tout d'abord, commençons par installer buildbot: easy_install -U buildbot
une fois ceci fait, il est désormais possible de créer des projets utilisant cet outil.
Pour ce faire, il suffit d'utiliser la commande suivante: paster create -t buildbot my.project
Un certain nombre d'informations seront demandées, saisissez donc la configuration qui vous convient.
Rendez-vous dans ce dossier, on observe ainsi son contenu :

bin bootstrap.py buildout.cfg  develop-eggs  master.cfg  parts  public_html slave.cfg

Le dossier bin contient le buildout ainsi que les différents processus maîtres/esclaves.
Ensuite, il est possible de remarquer que l'on dispose de bootstrap.py ainsi que
de buildout.cfg qui ont l'utilité habituelle.
parts contient quant à lui les fichiers des projets à construire, et public_html contient la css 
de l'affichage de buildbot.
Enfin, et non les moindres, les fichiers master.cfg ainsi que slave.cfg contiennent la configuration
des maîtres et des esclaves de buildbot.

Il nous faut ensuite construire l'environnement: python bootstrap.py puis ./bin/buildout.
Et enfin, nous pouvons lancer les démons maître/esclaves: ./bin/master start ainsi que ./bin/votrenomdemachine start

Vous avez désormais un buildbot fonctionnant à l'adresse http://localhost:9080/ par défaut.

**************************Documentation avancée*********************************

Pour des informations complètes sur l'utilisation des différentes recettes de 
buildout, veuillez vous réferer à la documentation officielle sur Pypi:
http://pypi.python.org/pypi/collective.buildbot/0.3.4





