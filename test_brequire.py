import sys
from twisted.trial import unittest

import brequire


class TestBrequire(unittest.TestCase):

	def _nukeAllRequires(self):
		brequire.allRequires = set()


	def test_requireFile(self):
		self._nukeAllRequires()
		self.addCleanup(self._nukeAllRequires)

		brequire.requireFile('path_a')
		# It's idempotent.
		brequire.requireFile('path_a')

		self.assertEqual(set([brequire.Require('path_a')]), brequire.allRequires)


	def test_requireFiles(self):
		self._nukeAllRequires()
		self.addCleanup(self._nukeAllRequires)

		brequire.requireFiles(['path_a', 'path_a', 'path_b'])
		# It's idempotent.
		brequire.requireFiles(['path_a', 'path_a', 'path_b'])

		self.assertEqual(set([
			brequire.Require('path_a'),
			brequire.Require('path_b'),
		]), brequire.allRequires)


	def test_publicAttr(self):
		"""
		Test that Require's public attributes return the right thing.
		"""
		req = brequire.Require('path_a')
		self.assertEqual('path_a', req.fpath)
