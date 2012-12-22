#!/usr/bin/env python3
# Filename: backup_ver1.py

import os
import time

os.path

# 1. The files and directories to be backed up are specified in a list.
source = [r'D:\Project', r'D:\ImagineCup']
# If you are using Linux, use source = ['/home/swaroop/byte', '/home/swaroop/bin']
# or something like that

# 2. The backup must be stored in a main backup directory
target_dir = 'D:\\backup\\' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.

# 4. The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d') + '.zip'
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
      comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)    # make directory
    print ('Successfully created directory', today)

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (target, ' '.join(source))
print (zip_command)
# Run the backup
if os.system(zip_command) == 0:
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')
