"""
Any module that needs non-Python-module files to work correctly should import
this module, and call requireFile at module scope like this:

requireFile(FilePath(__file__).sibling('some_file'))

This allows bpackage to know which static files are necessary for each
individual module.  (The distutils setup.py approach of setting package_data=
is not fine-grained enough.)

Any module that imports brequire *must* be safe to import (i.e., it does not
actually "do anything" on import).  Existing software (incl. Deepfreezer)
relies on this guarantee.
"""

__version__ = '10.11.15'

import operator


allRequires = set()


class Require(tuple):
	# http://ludios.org/ivank/2010/11/a-template-for-immutable-python-objects/
	__slots__ = ()
	_MARKER = object()

	fpath = property(operator.itemgetter(1))

	def __new__(cls, fpath):
		return tuple.__new__(cls, (cls._MARKER, fpath))


	def __repr__(self):
		return '%s(%r)' % (self.__class__.__name__, self[1])



def requireFile(fpath, frm=None):
	"""
	C{fpath} is a C{str} representing an absolute file path.
	"""
	import inspect
	if frm is None:
		# We don't really *need* to know the calling module, because
		# bpackage doesn't use the information, but we do it because
		# the debug info might be useful in the future.
		frm = inspect.stack()[1]
	module = inspect.getmodule(frm[0])
	require = Require(fpath)
	allRequires.add(require)
	##print "%r required %r" % (mod, f)


def requireFiles(fpaths):
	import inspect
	frm = inspect.stack()[1]
	for fpath in fpaths:
		requireFile(fpath, frm)
