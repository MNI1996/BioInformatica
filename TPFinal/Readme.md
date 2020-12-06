# ***A N A L I Z E***

#### (La aplicación fue programada en Windows 10)
### PRECONDICIONES
##
#### 1-) Instalar BLASTP (verificar las variables de entorno) con su correspondiente DB elegida (para instalar BLASTP: *https://www.ncbi.nlm.nih.gov/books/NBK52637/*)
	1-1) Si ud cuenta con windows 10 o powerShwell 3.0, puede ejecutar el bach de nombre "instal_db"
	1-2) Al descargarse manualmente la DB debe descomprimir la carpeta en otra ubicada en backend\db
#### 2-) Instalar Clustal (verificar las variables de entorno) (*http://www.clustal.org/omega/#Download*)
#### 3-) Conocer la ruta dónde se instaló Clustal, es necesaria para poder correr la aplicación ya que se le va a solicitar (por ejemplo: "C:\\Program Files (x86)\\ClustalW2\\clustalw2"
##
##
### BACKEND
#
#### 4-) Tener instalado python 3.6 (*https://www.python.org/downloads/windows/* y seleccionar la opción correspondiente)
#### 5-) Instalar biopython (*https://biopython.org/wiki/Download/*)
#### 6-) Instalar logomaker (*https://academic.oup.com/bioinformatics/article/36/7/2272/5671693*)
#### 7-) Instalar flask (*https://flask.palletsprojects.com/en/1.1.x/installation/*)
#### 8-) Instalar flaskCors (*https://pypi.org/project/Flask-Cors/*)
##
##
### FRONTEND
#
#### 9-) Instalar NodeJS (*https://nodejs.org/es/download/*)
##
##
### CÓMO SE USA LA APLICACIÓN
##
#### Para el correcto funcionamiento de la aplicación se deben correr los comandos desde las siguientes rutas:
#### 10) Para el **backend**: desde la carpeta TPFinal, escribir *python backend\apy.py*
#### 11) Para correr el **frontend**: desde la carpeta TPFinal, *escribir frontend\npm run dev*
##
#### 12-) Para visualizar las estructuras terciaria y cuaternaria se debe seleccionar de la pestaña *STYLE, protein, sphere*
##
#### 13-) Para visualizar la estructura secundaria desde la terciaria, se debe seleccioanr la pestaña, *STYLE, protein, ribbon*



