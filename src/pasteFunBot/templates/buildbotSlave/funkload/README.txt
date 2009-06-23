=============================================================================
                                  Funkload
                      Logiciel de test de montée en charge
=============================================================================

*************************Prérequis****************************

Python => python-dev, python-setuptools ainsi que python-xml
Paquet pour réaliser les graphes => gnuplot

***********************Installation***************************

=> easy_install -U funkload

Une démo est présente lorsque vous téléchargez Funkload, pour l'installer il suffit d'utiliser
la commande suivante: fl-install-demo

*********************Fonctionnalités**************************

Funkload possède diverses fonctionnalités que voici:
=> Réaliser des tests de base, via le biais de la commande fl-run-test nom_du_fichier. 
   Le fichier est un fichier de test standard utilisé en langage python. Toutes les fonctions écrites dans le fichier seront exécutées.

=> Réaliser des tests de benching, en utilisant deux fonctionnalités: 
	=> fl-monitor-ctl fichier_conf_monitor, permettant de lancer le moniteur gèrant les threads envoyés pour le test de bench
	=> fl-run-bench fichier_de_test nom_de_la_classe.nom_de_la_fonction_a_effectuer

=> Réaliser des rapports de benching en utilisant la commande fl-build-report nom_du_fichier_source.xml, il faut savoir que lors de
   fin des tests, un fichier contenant les résultats des tests est créé. Cette commande permet d'afficher une version plus claire sur la
   sortie standard.
   Cependant il existe diverses options à cette commande:
	=> --html, permet d'obtenir un rapport "graphique"
	=> --diff, permet de réaliser un rapport différentiel entre deux rapports réalisés avec l'option --html, il faut donc passer en 
	paramètre deux dossiers.

=> Enregistreur de tests: Cette fonctionnalités permet de réaliser des fonctions de tests très simplemenent en effectuant les tâches à tester
"à la main". Pour se faire, la première chose à faire est d'exécuter la commande fl-record nom_de_mon_test. Cette dernière va permettre de démarrer
l'écoute sur le port 8090 (par défaut), il faut donc changer le proxy en le définissant ainsi: localhost:8090.
Vous pouvez désormais réaliser toute sorte d'opérations sur votre site à tester. Une fois ceci fait, retournez sous la console et terminez l'enregistrement
en faisant ctrt+c, il en résultera un fichier test_nom_de_mon_test.py.
Enfin pour réaliser les tests, vous pouvez utiliser la commande fl-run-test -dV test_nom_de_mon_test.py et vous verrez toutes les étapes de votre test
réalisé dans votre navigateur.

=>Réaliser des tests sur des applications nécéssitant une identification. Pour celà, nous utilisons un serveur distribuant des identifiants et mots de passe
nommé serveur credential. Il nous faut donc donner de quoi travailler à ce serveur. Il faut rédiger deux fichiers distincts: passwd.txt et group.txt
ayant la même syntaxe que ceux du système de fichier unix, à savoir:
passwd.txt:
	login1:pwd1
	...

group.txt:
	group1:user1, user2
	group2:user3
	...
  Il suffit ensuite de lancer le serveur de credential avec la commande fl-credential-ctl fichier_conf_credential
=> Réaliser des tests en utilisant des fonctionnalités xmlrpc: quelques fonctions de base utilisant le protocole xmlrpc sont disponibles dans la classe de tests.

******************Implémentation de funkload******************
(des fichier d'exemples sont disponibles dans la démo, obtensible via la commande fl-install-demo)

Tests simples:
--------------
Pour implémenter des tests simples sous funkload, il faut rédiger deux fichiers:
	=> le premier est un fichier contenant les tests à exécuter, la classe qu'il contient doit hériter de FunkLoadTestCase, importable avec 
"from funkload.FunkLoadTestCase import FunkLoadTestCase"
	=> le second est un fichier de configuration contenant les données concernant le site à tester, les adresses à parcourir et autres.

Benching:
---------
Pour réaliser du benching simple, il vous faut trois fichiers distincts cette fois-ci:
	=> tout d'abord, les deux précédemment cités dans les "Tests Simples"
	=> le troisième est le fichier contenant la configuration du monitor qui s'occupe de la gestion des threads envoyés à l'application à tester

Credential:
-----------
Pour mettre en place ce type de tests, il est nécéssaire d'utiliser quatre fichiers:
	=> le premier est le fichier contenant les tests
	=> le second est un fichier de configuration du credential (credential.conf)
	=> enfin les deux derniers sont les fichiers passwd.txt et group.txt contenant les login et mot de passe à utiliser pour se connecter aux applications testées

Credential + benching:
----------------------
Pour réaliser ce genre de test, il vous suffit de combiner les fichiers de benching et de credential pour permettre des tests de benching avec authentification des utilisateurs.
