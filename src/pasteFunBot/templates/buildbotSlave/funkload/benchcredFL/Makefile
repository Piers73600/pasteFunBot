# Credential test with benching makefile

# Command line to launch the monitor and credential
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
# make_reports is the script used to generate the funkload reports
# and to send it by mail
    ../make_reports.sh cmf-bench.xml 
