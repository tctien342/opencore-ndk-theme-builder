from os import system as sh
import os
import argparse
parser = argparse.ArgumentParser(description='''
NDK's Opencore themes builder''', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', nargs='*', metavar='k=v',
                    help='Name of output zip files')
sh("rm -rf ./output")
sh("mkdir -p ./output")
for file in os.listdir("./icons"):
    if file.endswith(".png"):
        sh("/usr/bin/sips -z {} {} ./icons/{}".format(256, 256, file))
        print(os.path.join("./icons/", file))
        sh("cp ./icons/{} ./output/{}.icns".format(file, file.split(".")[0]))
sh("cp ./misc/* ./output/")
if parser.parse_args().n and len(parser.parse_args().n) > 0:
    zipName = parser.parse_args().n[0]
else:
    zipName = "build"
sh("zip -j {}-$(date +%y%m%d)-themes.zip ./output/*".format(zipName))
