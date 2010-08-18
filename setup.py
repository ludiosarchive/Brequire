#!/usr/bin/env python

from distutils.core import setup

import brequire

setup(
	name='brequire',
	version=brequire.__version__,
	description="A small module that collects 'I need this file to operate correctly' declarations. The bpackage tool uses this information.",
	py_modules=['brequire'],
)
