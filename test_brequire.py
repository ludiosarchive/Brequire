import sys
from twisted.trial import unittest
from twisted.python.filepath import FilePath

import brequire


class TestBrequire(unittest.TestCase):

	def _nukeAllRequires(self):
		brequire.allRequires = set()


	def test_requireFile(self):
		self._nukeAllRequires()
		self.addCleanup(self._nukeAllRequires)

		brequire.requireFile(FilePath('a'))
		# It's idempotent.
		brequire.requireFile(FilePath('a'))

		thisModule = sys.modules[__name__]
		self.assertEqual(set([brequire.Require(thisModule, FilePath('a'))]), brequire.allRequires)


	def test_requireFiles(self):
		self._nukeAllRequires()
		self.addCleanup(self._nukeAllRequires)

		brequire.requireFiles([FilePath('a'), FilePath('a'), FilePath('b')])
		# It's idempotent.
		brequire.requireFiles([FilePath('a'), FilePath('a'), FilePath('b')])

		thisModule = sys.modules[__name__]
		self.assertEqual(set([
			brequire.Require(thisModule, FilePath('a')),
			brequire.Require(thisModule, FilePath('b')),
		]), brequire.allRequires)
