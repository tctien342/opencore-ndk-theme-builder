from os import system as sh
import os
import argparse
parser = argparse.ArgumentParser(description='''
NDK's Opencore themes builder''', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', nargs='*', metavar='k=v',
                    help='Name of zip files')
sh("rm -rf ./Icons")
sh("mkdir -p ./Icons")
for file in os.listdir("./logo"):
    if file.endswith(".png"):
        sh("/usr/bin/sips -z {} {} ./logo/{}".format(256, 256, file))
        print(os.path.join("./logo/", file))
        sh("cp ./logo/{} ./Icons/{}.icns".format(file, file.split(".")[0]))
sh("cp ./misc/* ./Icons/")
if parser.parse_args().n and len(parser.parse_args().n) > 0:
    zipName = parser.parse_args().n[0]
else:
    zipName = "build"
sh("zip -r {}-$(date +%y%m%d)-themes.zip ./Icons/*".format(zipName))
