# chatbot
Chatbot desarrollado con Rasa, FastAPI, PostgreSQL, React (en proceso), un reverse proxy en Nginx, y todo se ejecuta mediante docker.
  
## **Instalación:**  
Para probar el chatbot debe tener instalado docker, una vez con eso listo clone el proyecto:  
```bash  
git clone https://github.com/zchelalo/chatbot.git
```  
  
Antes de continuar debe tener en cuenta que el nombre de la base de datos, la contraseña y el host vienen predefinidos en el archivo "docker-compose.yml", si quiere hacer algún cambio deberá hacerlo en ese archivo.  
  
A continuación puede cambiar la JWT_KEY del archivo ".env.example" por una más segura, esta se utiliza para la autenticación de los usuarios.  
  
Seguido de esto solo cambie el nombre del archivo ".env.example" quitandole el ".example".  
  
Despues de ello asegurese de estar dentro de la carpeta del proyecto y ejecute el siguiente comando:  
```bash  
docker compose up
```  
  
Es posible que según la versión de docker que tenga o donde lo tenga, tendrá que ejecutar el siguiente comando en lugar del anterior:  
```bash  
docker-compose up
``` 
  
Despues de que se haya hecho la build y esten en ejecución los servicios de nginx, fastapi, rasa, postgres y react (de momento no esta), es momento de probar el chatbot en la URL [http://localhost/fastapi](http://localhost/fastapi) en la cual esta alojado el servidor de fastapi por el cual se entrena al bot y se interactua con él.
  
## **Documentación:**  
Para poder ver la documentación a la vez que probar la API REST del chatbot nos podremos dirigir a [http://localhost:8000/docs](http://localhost:8000/docs) una vez que nuestro servidor este activo.  
  
En esta ruta se podrán ver todos los endpoints de la API y podremos probar cada uno de ellos desde ahí mismo, siendo esto muy útil a la hora de testear.  
  
Se utiliza Swagger para documentar la API, de esta forma se ordenan los endpoints en bloques a la misma vez que se documenta su utilidad y funcionamiento.  
  
Para poner en funcionamiento el sistema necesita hacer lo siguiente:  
1. Primeramente creará un usuario en su correspondiente endpoint, este no necesitará de autenticación la primera vez.  
2. Después se dirigirá al endpoint de auth, en el cual ingresará sus credenciales (email, password), y si todo salio bien le devolverá un token.
3. Copiará el token recibido y dará click en el boton de authorize (tambien puede hacerlo dando click en los candaditos que hay en cada endpoint).  
  
![Muestra del botón](/img/img-auth.png)  
  
4. Seguido de esto ingresará el token copiado en el campo que se muestra a continuación:  
  
![Muestra autenticación](/img/img-auth-2.png)  
  
5. Con esto hecho solo de click en "Authorize" y podrá probar la aplicación. Tome en cuenta que el proceso de poner el token de autenticación lo tendrá que repetir cada que recargue la página.  
  
## **Funcionamiento del chatbot**
Para poner en funcionamiento el chatbot primero ingrese en la base de datos intents, responses, rules, steps_rule, stories y steps_story.  
  
Seguido de esto genere los siguientes archivos: domain.yml, nlu.yml, rules.yml e stories.yml, tenga en cuenta que ya existen unos endpoint en la API de FastAPI que hacen esto con solo hacer una petición POST.  
  
Después creará el modelo para el chatbot, parará el proceso de rasa y cuando termine totalmente lo iniciará de nuevo. Solo queda probar el chatbot enviandole algún mensaje mediante su endpoint correspondiente.