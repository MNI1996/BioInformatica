# ***A N A L I Z E R***

##### Analize es un visualizador de proteínas con sus estructuras y conservación, tomando como parámetro de ordenamiento de conservación, el porcentaje de identidad. Con sólo ingresar el código PDB de la proteína, la dirección local dónde se instaló CLUSTAL y setear algunos parámetros, permite visualizar las estructuras primaria, secunaria, terciaria y cuaternaria (si la tiene) de la proteína ingresada, además de las cadenas homólogas alineadas.

##### Por medio de un visalizador es que se puede observar las estructuras terciarias y cuaternarias de diferentes maneras

##### La aplicación fue programada para ser usada en Windows 10
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
#### - Tener instalado python 3.6 (*https://www.python.org/downloads/windows/* y seleccionar la opción correspondiente)
#### - Instalar biopython (*https://biopython.org/wiki/Download/*)
#### - Instalar logomaker (*https://academic.oup.com/bioinformatics/article/36/7/2272/5671693*)
#### - Instalar flask (*https://flask.palletsprojects.com/en/1.1.x/installation/*)
#### - Instalar flaskCors (*https://pypi.org/project/Flask-Cors/*)
##
##
### FRONTEND
#### - Instalar NodeJS (*https://nodejs.org/es/download/*)
##
##
### CÓMO SE USA LA APLICACIÓN
#### Para el correcto funcionamiento de la aplicación se deben correr los comandos desde las siguientes rutas:
#### + Para el **backend**: desde la carpeta TPFinal, escribir *python backend\apy.py* y tiene que notificar lo siguiente en la consola de PyCharm:
	 * Serving Flask app "api" (lazy loading)
	 * Environment: production
	   WARNING: This is a development server. Do not use it in a production deployment.
	   Use a production WSGI server instead.
	 * Debug mode: on
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 267-229-492
	 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#### + Para correr el **frontend**: desde la carpeta TPFinal, *escribir frontend\npm run dev*. Luego de compliar, le notifica lo siguiente:*i ｢wdm｣: Compiled successfully*.
#### + Para ingresar al HOME, se debe abrir una pestaña nueva del navegador y escribir *"http://localhost:8080"*.
#### + En el HOME se encuentra una pantalla donde ingresan los datos:
		-) ingresar el código PDB de la proteína, 
		-) la ruta dónde se instaló CLUSTAL (hay un ejemplo en la parte inferior del cuadro de diálogo). 
		-) definir el word size entre 3 (viene por default), 6 y 12 
		-) definir el número de muestras entre 5 (viene por default), 10 y 15
		-) ingresar el e-value (por default está seteado 0.001)
		-) ingresar la penalidad de gaps (por default está seteado 11)
		-) Ingrese % de identidad minimo deseado que por default está seteado 39.9
#### + Luego de mostrar la estructura primaria de la proteína ingresada, se presenta un visualizador con la representación de la estructura terciaria.
#### + La visualización de las estructuras terciaria y cuaternaria, por default es *Ribbon*. Para cambiarla, se debe seleccionar de la pestaña *STYLE, protein, sphere*, por ejemplo. 
#### + Para visualizar estructura secundaria se debe seleccioanr la pestaña, *STYLE, protein, ribbon*



