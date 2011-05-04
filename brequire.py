"""
Any module that needs non-Python-module files to work correctly should import
this module, and call requireFile at module scope like this:

requireFile(FilePath(__file__).sibling('some_file').path)

or if you don't want to use filepath.FilePath:

requireFile(os.path.join(os.path.dirname(__file__), 'some_file'))

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
	Declare that C{fpath} is necessary for the program to work.  C{fpath}
	should be a file inside one of your C{sys.path} directories.

	@param fpath: a C{str} or C{unicode} representing an absolute file path.
	"""
	allRequires.add(fpath)


def requireFiles(fpaths):
	"""
	Declare that every path in C{fpaths} is necessary for the program to
	work.  Each path should be a file inside one of your C{sys.path}
	directories.

	@param fpaths: an iterable of C{str} or C{unicode}, each representing an
		absolute file path.
	"""
	for fpath in fpaths:
		requireFile(fpath)
