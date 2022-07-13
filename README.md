# Entrega1-Tarela-y-Arrighi
Integrantes de este proyecto: Arrighi Alejandro y Tarela Galante Francisco

Pasos a seguir

1) Abrir VSCode, en la terminal posicionarse sobre la ruta ejecutando el comando cd y la ruta donde fue creada la carpeta que contiene el proyecto, en este caso seria cd C:\%usersprofile%\Desktop\Visual Coderhouse\ProyectoFamilia

2) Una vez posicionado levantar el servidor ejecutando el comando: python manage.py runserver. Esperar que cargue y aparecera un link a la ip 127.0.0.1:8080 (localhost). Entrar a dicha url y modificar la misma para que quede http://127.0.0.1:8000/FamiliaApp/

3)Dentro de la pagina podran cargar en los formularios correspondientes a su auto, mascota o familiar deseado. Luego pueden buscarlo con los botones que se encuentran al lado de los formularios. 
DISCLAIMER: (Los datos ingresados son distinguen entre mayusculas y minusculas, tener eso en consideracion al momento de realizar la busqueda deseada)

Funcionalidades:

Pasemos al back end dentro de VSCode:

Si bien hay muchos files podriamos resumirlo en 3 grandes grupos caracteristicos. MTV (Model Template View)
DISCLAIMER: Estas definiciones solo aplican para Django (cambian en otras plataformas)

Model: Es la parte que almacena la informacion y maneja el caudal de datos. (Base de datos).

-Entramos a models.py y configuramos las Clases con los valores a futuro a rellenar en los formularios. (no olvidarse, siempre de Importar y guardar)

Template: Es la parte que visualiza el usuario. Son archivos que permiten modificar la estructura/estetica/visualizacion de nuestra pagina/app. 

-Se crea la estructura en formato .html (se puede usar una estructura default poniendo ! o html:5) Y en ella se modifica, el titulo, colores de letras,tamaño de estas, etc etc. Cuenta con un template Padre o Main del cual se pueden heredar sus configuraciones para los demas templates(conocidos como hijos).(no olvidarse, siempre de Importar y guardar!!)

View: es nuestro controlador encargado de transferir la informacion desde el usuario hasta la DataBase(Model) y viceversa (en este último el proceso sería enviar enviandosela al Template). Entramos a views.py y configuramos las funciones que querramos mostrar en el template. (no olvidarse, siempre de Importar y guardar!!)

-La estructura básica de estas sería : def nombrefuncion (request): 
return render (pagina.html). Es decir: defino la funcion llamada X, y solicito: devolver un render(transformacion a pagina web) con un formato .html.

URL: es Uniform Resource Locator. es decir es la dirección única y específica que se asigna a cada uno de los recursos disponibles. En el archivo Urls.py es donde vamos a configurar el nombre que se va a usar para llamar a las funciones del view, los template y a su vez con que nombre se accede a las distintas opciones de la pagina web. (nombre de redireccion).

forms.py: Vistas que permiten agregar datos a nuestro model desde la web. Existen dos metodos para que la información viaje hasta nuestro servidor, GET y POST. (para informacion extra de get y post ver clase 21, filmina 11)
