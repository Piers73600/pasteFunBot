#Makefile de funkload

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
	../make_reports.sh simpleFL/ simple-bench.xml
