#tui tạo 2 file sh một để upzip từng cái, một dùng loop
#!/bin/bash

for i in {1..101}; do
    # Execute the command
    ./hack.sh
done
---------------------------------------------------
#!/bin/bash

for i in {1..101}; do
    # Execute the command
    ./hack.sh
done
hackervnn40@cloudshell:~/kon (western-mix-340011)$ cat hack.sh
#!/bin/bash

# Path where the zip file is located
ZIP_PATH='/home/hackervnn40/kon/'

# Write the password here
PASSWORD='Arez'

# Unzip all the files in the zip path
for f in $ZIP_PATH/*.zip; do
    unzip -P $PASSWORD -o $f
done
