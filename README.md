https://github.com/BlaZzes10/SSDD-GarciaGuerreroMarroquin/tree/L2

Tomás Jesús García López (BlaZzes10) tomasjesus.garcia@alu.uclm.es

Pablo Guerrero Sanjuan (Blapo1) pablo.guerrero@alu.uclm.es

Anderson Marroquín Rivas (anderRSTN59) anderson.marroquin@alu.uclm.es


## ¿Cómo Desplegar La Aplicación?
### Primer Paso
Primeramente, nosotros ejecutamos nuestro prepare_distribution creando los directorios node1 y 2, hemos comentado esas lineas ya que se supone que ya estaran creados previamente.
### Segundo Paso
Posteriormente abrimos la aplicación en Icegrid y cargamos el archivo icegauntlet.xml
### Tercer Paso
Continuamos pasando la Aplicación al Live Deployment. Hay que tener cuidado que al pasarlo los Servidores de RoomManager y Dungeon aparecerán inactivos, esto es porque configuramos que siempre esten activos y al cargar la aplicación se intentan activar **Sin antes tener el IcePath2 cargado**
### Cuarto Paso
Cargamos el Path Distribution y ya podremos lanzar los servidores, Nosotros primero lanzamos siempre el AuthServer o el IceStorm, da igual el orden pero tienen que ser los primeros.
Posteriormente hay que habilitar los servidores de RoomManager y el Dungeon -> Click Derecho y Enable. Estan al principio inactivos por lo que he comentado antes y es posible que en el log de los icegridnode aparezca un Warning, pero funcionan perfectamente al seguir estos pasos, Sin problema.
### Quinto Paso
A partir de aquí ya se pueden ejecutar todos los scripts para comprobar el perfecto comportamiento de los servidores esperado para el entregable L2 

### Pequeña Nota
Los servidores se despliegan automaticamente gracias al campo activation = always. Entonces dará un warning en los nodos 1 y 2.
Se vuelven a activar con el campo enabled y ya funcionan correctamente. Es la manera en la cual nos funcionaba el servicio IceStorm, poniendo los servidores activados always.
