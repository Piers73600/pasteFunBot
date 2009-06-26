#!/bin/bash
# Exemple d'un fichier de test avec un projet turbogears
# A placer dans le dossier de build du projet

# Lancement du serveur de l'application (specifique a turbogears)
paster serve development.ini >> log.txt &
# On recupere le pid afin de pouvoir l'arreter automatiquement une fois nos tests finis
pid=`echo $!`
# On laise quelques secondes au serveur pour demarrer
sleep 5
# On se rend dans le dossier contenant les tests a realiser car la commande
# fl-run-test ne prend en parametre que des fichiers du repertoire actuel
cd ./funkload/simpleFL/
# On lance les tests dis "simples"
fl-run-test test_Simple.py

# Ensuite, on desire lancer un benching
# On lance ainsi le demon de monitoring
fl-monitor-ctl monitor.conf restart
# On lui laisse un peu de temps pour demarrer
sleep 5
# On lance les tests de benching (cf README.txt de Funkload)
fl-run-bench test_Simple.py Simple.test_Simple
# Une fois les tests realises, on coupe le demon de monitoring
fl-monitor-ctl monitor.conf stop
# On change de repertoire pour realiser les rapports
cd ..
# On utilise le script de generation de rapports en lui passant en parametre 
# le nom du dossier de test ainsi que le nom du fichier .xml contenant les infos
# des tests, et enfin on arrete le serveur de l'application
./make_reports.sh simpleFL/ simple-bench.xml && kill $pid
