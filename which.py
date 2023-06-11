#!python3
import os, sys
import glob

class x_finished (Exception): pass

paths = ["."] + [os.path.expandvars(p) for p in os.environ.get ("PATH", "").split (";")]
exts = [e.lower () for e in os.environ.get ("PATHEXT", ".exe").split (";")]

if __name__ == '__main__':
  if len (sys.argv) > 1:
    search_for = sys.argv[1]
  else:
    search_for = raw_input ("Search for:")

  base, ext = os.path.splitext (search_for)
  if ext:
    exts = [ext]

  paths_seen = set()
  for path in paths:
    if path.lower() in paths_seen:
      continue
    else:
      paths_seen.add(path.lower())

    for ext in exts:
      filepath = os.path.join (path, "%s%s" % (base, ext))
      filenames = glob.glob (filepath)
      if filenames:
        for filename in filenames:
          print filename
