import os,platform
os.system("git pull")
rmx=platform.architecture()[0]
if rmx=='64bit':
  import ILYM
if rmx=='32bit':
  import ILYR
else:print('\033[1;32m[•] Contract Admin For Help');exit()
  
 
