# TwitterStatusExtractor
A small library to extract status id from the given twitter account

# Usage

import the file tse.py in the same folder than your project,
then at the start of the file using the script use 
```import tse as tse```

# Functions

getStatusIds(user,nbStatus=3,headless=True) where user is the name of the twitter account without the @ :
  retrieve the last nbStatus for the given user
  
getStatusMultipleUsers(listUsers,nbStatus=3,headless=True):
  retrieve the last nbStatus for each user in the listUsers
