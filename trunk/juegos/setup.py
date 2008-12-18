# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(name="Demostración de pygame",
      version="0.2",
      description="Programa de ejemplo de pygame",
      author="clase de programación",
      license="GPL",
      windows = [
          {'script': "figuras.pyw",
           'icon_resources':[(1, 'python.ico')]}
          ],
      options = {"py2exe": {"bundle_files":1 }},
      zipfile = None
      )