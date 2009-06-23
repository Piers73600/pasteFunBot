import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import xmlrpc_get_credential, xmlrpc_list_credentials
from funkload.Lipsum import Lipsum

class CmfTestCase(FunkLoadTestCase):
	
	def cmfLogin(self, login, pwd):
		params = [["login", login],
			  ["password", pwd],
			  ["submit", "Login"]]
		
		self.post('%s/login_handler?_logins=0&came_from=/' % self.server_url, params, description="Login utilisateur %s" % login)
		self.assert_('Welcome' in self.getBody(), "Credential invalide %s:%s" % (login, pwd))
		self._cmf_login = login


class Cmf(CmfTestCase):

	def setUp(self):
		self.logd("setUp")
		self.server_url = self.conf_get('main', 'url')
		credential_host = self.conf_get('credential', 'host')
		credential_port = self.conf_getInt('credential', 'port')
		self.credential_host = credential_host
		self.credential_port = credential_port
		self.cred_manager = xmlrpc_get_credential(credential_host, 
							  credential_port,
							  'managers')

	def test_01_connect(self):
		server_url = self.server_url
		self.cmfLogin(*self.cred_manager)

	def tearDown(self):
		self.logd('tearDown.\n')

if __name__ in ('main', '__main__'):
	unittest.main()
