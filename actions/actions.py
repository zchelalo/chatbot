from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

ruta_server = "http://localhost:3000/"
ruta_img = ruta_server + "img/"
ruta_pdf = ruta_server + "pdf/"

class ActionReinscripcion(Action):
	def name(self) -> Text:
		return "action_reinscripcion"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		texto = 'Para reinscribirte primero tienes que ingresar al sitio web del SIAGE UTN (https://siageescolar.net/estudiantes_utnogales/). Después de eso tendras que dar click en la sección de "Reinscripción" como se señala en la siguiente imagen:'

		texto2 = 'Después de haberlo hecho se te descargará un archivo en formato PDF, este contiene datos como tu referencia y el número de convenio CIE. Con esos datos tendrás que ir a un cajero automático o pagar desde la aplicación BBVA. Utilices el método que sea, los pasos son los mismos:'

		texto3 = '1: Selecciona la opción de "Pagar servicio o impuesto".'
		texto4 = '2: Ingresa el número de convenio CIE.'
		texto5 = '3: A continuación tendrás que escribir tu número de referencia cuando te lo pida.'
		texto6 = '4: Después agregaras el costo de la reinscripción el cual viene en el PDF descargado con anterioridad.'
		texto7 = '5: Cuando se efectue el pago recuerda el imprimir el ticket en caso de ir al cajero automático, en caso de haber pagado desde la aplicación toma captura del movimiento efectuado.'

		response = [
				[
					texto,
					ruta_img + "reinscripcion-paso-1.png",
				],
				texto2,
				[
						texto3,
						texto4,
						texto5,
						texto6,
						texto7
				]
		]

		dispatcher.utter_message(json_message=response)

		# dispatcher.utter_message(text="¡Claro! Tiene que hacer lo siguiente")

		# URL de la imagen
		# imagen_url = "https://ejemplo.com/ruta/a/la/imagen.png"
		# dispatcher.utter_custom_json({"image": imagen_url})

		return []

class ActionCalendario(Action):
	def name(self) -> Text:
		return "action_calendario"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		texto = 'En el siguiente calendario podrás ver distintos tipos de fechas, como de las inscripciones, cursos de inducción, inicio del cuatrimestre, fin del cuatrimestre, reinscripciones, vacaciones, días inhabiles, días habiles, etcétera.'

		response = [
			[
				texto,
				ruta_pdf + "calendario.pdf"
			]
		]

		dispatcher.utter_message(json_message=response)

		return []

class ActionProcesoEstadias(Action):
	def name(self) -> Text:
		return "action_proceso_estadias"

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		texto = 'El procedimiento para llevar a cabo las estadías es el siguiente:'

		texto2 = '1: Primeramente encontrar una empresa que te admita como practicante o como trabajador en la cual desarrollar tu proyecto de estadías (esta tendrá que estar registrada en el SAT, de lo contrario no se podrán validar tus estadías).'
		texto3 = '2: Seguido de lo anterior tendrás que entregar una carta para el convenio entre la empresa y la Universidad Tecnológica de Nogales (si anteriormente algún alumno hizo sus estadías en dicha empresa, esta carta no será necesaria).'
		texto4 = '3: Ya con el registro hecho harás tu proyecto en la empresa y desarrollarás tu documento de estadías (tu asesor asignado te ayudará y apoyará en el desarrollo de este).'
		texto5 = '4: Una vez terminado tu proyecto, tu documento y tengas las horas necesarias para acabar las estadías (360 horas) tendrás que llevar tu carta de finalización de estadías a la empresa donde las hiciste para que la sellen y la firmen.'
		texto6 = '5: Con la carta firmada, la llevarás a tu dirección de carrera, junto con tu documento de estadías finalizado y revisado por tu asesor. El documento de estadías tiene que cumplir ciertas normas que cumplir y tiene que estar impreso.'
		texto7 = '6: Después de haber terminado todo y de que el director de carrera te valide las estadías, significa que las habrás acabado exitosamente. ¡Felicidades!'

		texto8 = 'Si tienes alguna duda no te la pienses dos veces en comentarmelo :)'

		response = [
			texto,
			[
				texto2,
				texto3,
				texto4,
				texto5,
				texto6,
				texto7
			],
			texto8
		]

		dispatcher.utter_message(json_message=response)

		return []