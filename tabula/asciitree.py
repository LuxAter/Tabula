#!/usr/bin/env python

import clang.cindex, asciitree, sys

clang.cindex.Config.set_library_path("/usr/lib/llvm-5.0/lib/libclang.so")
index = clang.cindex.Index(clang.cindex.conf.lib.clang_createIndex(False, True))
translation_unit = index.parse(sys.argv[1], ['-x', 'c++'])

print asciitree.draw_tree(translation_unit.cursor,
  lambda n: n.get_children(),
  lambda n: "%s (%s)" % (n.spelling or n.displayname, str(n.kind).split(".")[1]))
