"""
Any module that needs non-Python-module files to work correctly should import
this module, and call requireFile at module scope like this:

requireFile(FilePath(__file__).parent().child('some_file'))

This allows bpackage to know which static files are necessary for each
individual module.  (The distutils setup.py approach of setting package_data=
is not fine-grained enough.)

Note: bpackage thinks that anything that imports this module is safe to import.
"""

__version__ = '10.8.18'

import operator


allRequires = set()


class Require(tuple):
	# All the strange stuff here is just to make an immutable object
	# (which is also nicely __eq__'able).
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
