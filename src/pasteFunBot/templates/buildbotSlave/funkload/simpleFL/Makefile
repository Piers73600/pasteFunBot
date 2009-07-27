# Funkload makefile

MONCTL := fl-monitor-ctl monitor.conf

all: test
test: simple_test

simple_test:
	fl-run-test test_Simple.py

bench: simple_bench

simple_bench:
	$(MONCTL) restart
	fl-run-bench test_Simple.py Simple.test_simple
	$(MONCTL) stop
# make_reports is the script used to generate the funkload reports
# and to send it by mail
	../make_reports.sh simple-bench.xml
