#!/usr/bin/env python

from distutils.core import setup

import brequire

setup(
	name='Brequire',
	version=brequire.__version__,
	description="A small module that collects 'I need this non-Python " +
		"file to operate correctly' declarations.",
	url="https://github.com/ludios/Brequire",
	author="Ivan Kozik",
	author_email="ivan@ludios.org",
	classifiers=[
		'Programming Language :: Python :: 2',
		'Development Status :: 5 - Production/Stable',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
	],
	py_modules=['brequire'],
)
