# Aún en desarrollo  
## -- BACKEND --  
- [ ] Crear la base de datos para entrenar al bot desde ella.  
  
- [ ] Añadir una tabla de mensajes la cual tendrá como finalidad el registrar los mensajes enviados por usuario y bot. Está tendrá campos como ID, clave, rol del mensaje (bot o usuario), contenido del mensaje, fecha y hora del mensaje.  
Así puedo crear historias realistas al chatbot. Claro, con el contenido del mensaje por parte del usuario obtengo la intención del bot, después comparo la respuesta del bot con la proporcionada, si son iguales se da como positivo y se puede continuar con la creación de la story, si da negativo no se creará una story con esa serie de mensajes.  
  
- [ ] Añadir una tabla de calificación, en esta a la hora de que se califique un mensaje ya sea de forma positiva o de forma negativa, se registrará en la base de datos. Tendrá ID, ID intención, mensaje usuario, calificación (positiva o negativa), fecha y hora de la calificación.  
Cuando se califique un mensaje, este le hablará a algún método de la API, en el cual se le enviará tanto el mensaje del usuario como del bot, con el fin de sacar la intención desde la API ya que no la da directamente, se compararán las respuesta del bot para saber si son iguales y así guardar la información.  
  
## -- FRONTEND --  
- [ ] Primeramente, el chatbot estará presente en la gran mayoría de las páginas, en forma de un pequeño icono en la esquina inferior derecha de la pantalla, así se tiene acceso a él de una forma cómoda y con disponibilidad en todo momento.  
  
- [ ] Al momento de clikear en él se cambiara el icono de Grajillo por el de un símbolo de enviar, a la par que se abrirá el propio chat con un saludo y unas propuestas de mensaje para enviarle.  
  
- [ ] La interfaz reaccionará según sea necesario, si se necesita de una imágen, documento o instrucción, estarán. Estás se podrán clickar para abrirlas en grande, a la vez de poder descargarlas.  
  
- [ ] Abajo de cada mensaje o serie de mensajes por parte del bot habrá un recuadro alineado a la derecha el cual diga "¿Fue útil el mensaje?" con un icono de una manita hacia arriba y uno de manita hacia abajo, con el fin de calificar la respuesta del bot.  
  
*- Posibilidades a tomar en cuenta -*  
Existe la posibilidad de que cuando se califique un mensaje de forma negativa se guarde la respuesta del usuario como un ejemplo el cual no da ninguna respuesta. Al momento de guardar ejemplos sin intención en el archivo de NLU estos son considerados neutros o que no deben accionar ante ninguna intención.  