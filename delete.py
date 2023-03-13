def clean():
    import os, re, os.path
    mypath = "static/files"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))
    return
#clean()