import sys


class InstallPackage:
    def __init__(self):
        def install(package):
            try:
                __import__(package)
            except:
                import subprocess
                subprocess.call([sys.executable, "-m", "pip", "install", package])

        with open('res/requirement.txt') as f:
            for line in f:
                line = line.replace("\n", "")
                install(line)



