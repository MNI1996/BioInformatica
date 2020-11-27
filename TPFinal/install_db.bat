SET var=%cd%

if not exist %var%"\backend\db" mkdir %var%\backend\db
if not exist %var%"\backend\db\pdbaa.tar.gz" powershell -command "& { iwr https://ftp.ncbi.nlm.nih.gov/blast/db/pdbaa.tar.gz -OutFile backend/db/pdbaa.tar.gz }

tar xvf backend\db\pdbaa.tar.gz -C backend\db  

