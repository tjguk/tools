#!python3
import os, sys
import zipfile

def is_readable(filepath):
    try:
        open(filepath).close()
    except OSError:
        return False
    else:
        return True

def unzip(filepath):
    try:
        zf = zipfile.ZipFile(filepath)
    except:
        yield None, None
    else:
        for zi in zf.infolist():
            if not zi.is_dir():
                try:
                    with zf.open(zi) as f:
                        yield zi.filename, f.read()
                except:
                    yield None, None

def search(word, start_from="."):
    bword = bytes(word, encoding="utf-8")
    for dirpath, dirnames, filenames in os.walk(start_from):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if is_readable(filepath):
                if zipfile.is_zipfile(filepath):
                    for zname, zbytes in unzip(filepath):
                        if zname is None:
                            continue
                        if bword in zbytes:
                            print(filepath, "/", zname)
                else:
                    with open(filepath, "rb") as f:
                        if bword in f.read():
                            print(filepath)

if __name__ == '__main__':
    search(*sys.argv[1:])
