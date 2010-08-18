"""
Any module that needs non-Python-module files to work correctly should import
this module, and call requireFile at module scope like this:

requireFile(FilePath(__file__).parent().child('some_file'))

This allows bpackage to know which static files are necessary for each
individual module.  (The distutils setup.py approach of setting package_data=
is not fine-grained enough.)
"""

__version__ = '10.8.18'

import inspect


allRequires = []


class Require(object):
	def __init__(self, module, fpath):
		self.module = module
		self.fpath = fpath



def requireFile(fpath, frm=None):
	"""
	C{fpath} is a L{twisted.python.filepath.FilePath}.
	"""
	if frm is None:
		frm = inspect.stack()[1]
	module = inspect.getmodule(frm[0])
	require = Require(module, fpath)
	allRequires.append(require)
	##print "%r required %r" % (mod, f)


def requireFiles(fpaths):
	frm = inspect.stack()[1]
	for fpath in fpaths:
		requireFile(fpath, frm)
