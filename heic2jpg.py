# heic2jpg.py
# daisuke.t.jp@gmail.com
#
# Usage
# $ pyhton3 heic2jpg.py <HEIC DIR>

import sys
import os
import shutil
import subprocess
import pathlib

DST_DIR_NAME = 'jpg'

if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit('You must set the source directory.')

  srcDir = sys.argv[1]

  dstDir = os.path.join(srcDir, DST_DIR_NAME)
  if os.path.isdir(dstDir):
    shutil.rmtree(dstDir)
  
  os.makedirs(dstDir)

  array = os.listdir(srcDir)

  for elm in array:
    path = pathlib.Path(elm)
    
    if path.suffix.upper() != '.HEIC':
        continue
        
    srcFile = os.path.join(srcDir, path)
    dstFile = os.path.join(dstDir, path.stem + 'jpg')
    
    cmd = 'sips --setProperty format jpeg {0} --out {1}'.format(srcFile, dstFile)
    subprocess.call(cmd, shell=True)

  print('* The jpeg file was generated to {0}. *'.format(dstDir))
