#test de credential avec du benching

MONCTL := fl-monitor-ctl monitor.conf
CREDCTL := fl-credential-ctl credential.conf

all: test

#testing
test: bench_credential

bench_credential:
    $(MONCTL) restart
    $(CREDCTL) restart
    fl-run-bench test_Cmf.py Cmf.test_01_connect
    $(CREDCTL) stop
    $(MONCTL) stop
    ../make_reports.sh benchcredFL/ cmf-bench.xml 
