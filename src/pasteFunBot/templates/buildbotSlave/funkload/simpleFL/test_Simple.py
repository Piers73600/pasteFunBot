import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

class Simple(FunkLoadTestCase):

	def setUp(self):
		self.logd("setUp")
		self.server_url = self.conf_get('main', 'url')

	def test_simple(self):
		# la description doit etre mise dans le fichier de conf
		server_url = self.server_url
		# debut du test
		nb_time = self.conf_getInt('test_simple', 'nb_time')

		for i in range(nb_time):
			self.logd('Try %i' % i)	
			self.get(server_url, description='Get page principale de google')
		# fin du test

	def tearDown(self):
		self.logd("tearDown.\n")

if __name__ in ('main', '__main__'):
	unittest.main()
