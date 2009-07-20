# Credential test makefile

CREDCTL := fl-credential-ctl credential.conf

all: test

#test

test: credential_test

credential_test:
    $(CREDCTL) restart
    fl-run-test test_Cmf.py
    $(CREDCTL) stop 
