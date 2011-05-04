"""
Any module that needs non-Python-module files to work correctly should import
this module, and call requireFile at module scope like this:

requireFile(FilePath(__file__).sibling('some_file'))

This allows Deepfreeze to know which static files are necessary for each
individual module.  (The distutils setup.py approach of setting package_data
is not fine-grained enough.)

Any module that imports brequire *must* be safe to import (i.e., it does not
actually "do anything" on import).  Existing software (incl. Deepfreeze)
relies on this guarantee.
"""

__version__ = '11.5.4'


allRequires = set()

def requireFile(fpath):
	"""
	@param fpath: a C{str} or C{unicode} representing an absolute file path.
	"""
	allRequires.add(fpath)


def requireFiles(fpaths):
	for fpath in fpaths:
		requireFile(fpath)
