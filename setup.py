#!/usr/bin/env python

from distutils.core import setup

import brequire

setup(
	name='Brequire',
	version=brequire.__version__,
	description="A small module that collects 'I need this non-Python " +
		"file to operate correctly' declarations.",
	py_modules=['brequire'],
)
