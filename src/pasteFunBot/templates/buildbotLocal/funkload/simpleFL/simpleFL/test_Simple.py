import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

class Simple(FunkLoadTestCase):

	def setUp(self):
		self.logd("setUp")
		self.server_url = self.conf_get('main', 'url')

	def test_simple(self):
		server_url = self.server_url
		# Beginning of the test
		nb_time = self.conf_getInt('test_simple', 'nb_time')

		for i in range(nb_time):
			self.logd('Try %i' % i)	
			self.get(server_url, description='Get page principale de google')
		# End of the test

	def tearDown(self):
		self.logd("tearDown.\n")

if __name__ in ('main', '__main__'):
	unittest.main()
