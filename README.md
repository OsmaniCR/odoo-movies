# Películas

## Descripción general del módulo

Películas es un módulo para Odoo 17 que permite gestionar un catálogo de películas obteniendo información desde un servicio externo. Sus principales características incluyen:

- Integración con API externa: Recupera datos de películas desde una API externa mediante una tarea programada (cron) que se ejecuta cada minuto.
- Almacenamiento de películas: Registra y almacena la información de cada película en el modelo movie.movie dentro de Odoo (por ejemplo, título, ranking, etc.).
- Endpoint REST público: Expone un endpoint REST (/api/top_movies) que devuelve las 10 películas con mejor ranking (ordenadas descendentemente por este valor) en formato JSON.
- Parámetros de configuración: Permite configurar la URL del API externo y la clave de API (API Key) desde la interfaz de Ajustes de Odoo, facilitando la personalización sin cambiar el código.
- Compatibilidad con Docker: Diseñado para ejecutarse fácilmente en Docker – se proporciona un archivo docker-compose.yml para la puesta en marcha rápida del módulo junto con Odoo y los servicios necesarios.
- Interfaz en Odoo: Añade menús y vistas dentro de Odoo para visualizar y gestionar las películas registradas.

## Requisitos previos

Antes de instalar el módulo, asegúrate de contar con los siguientes requisitos:

- Docker y Docker Compose: Instalados en caso de querer ejecutar la instancia de Odoo usando el archivo docker-compose.yml proporcionado.
- API de películas: Credenciales de acceso a la API externa de películas (URL base del servicio y una API Key válida).

## Instrucciones de despliegue

\*\* Se utiliza make para ejecutar los comandos de manera más acotada (Opcional).

Despliegue con Docker Compose:

- Clona este repositorio o descarga el código fuente del módulo.
- Asegúrate de que en el directorio del proyecto se encuentra el archivo docker-compose.yml incluido. Este archivo define los servicios de Odoo 17 y PostgreSQL necesarios.
- Abre una terminal en dicho directorio y ejecuta:

  ```bash
  make run-dev
  ```

  o

  ```bash
  docker-compose up -d
  ```

  Esto descargará las imágenes de Docker necesarias y levantará los contenedores (base de datos y servidor Odoo) en segundo plano.

- Una vez que los contenedores estén en ejecución, accede a la interfaz web de Odoo abriendo tu navegador en http://localhost:8069. Aquí deberás crear la base de datos inicial.
- Inicia sesión en Odoo con las credenciales que definiste.
- Activa el modo desarrollador en Odoo (opcional pero recomendado).
- Navega a Aplicaciones y pulsa en Actualizar lista de aplicaciones para que Odoo detecte el nuevo módulo (en caso de que no aparezca directamente).
- Busca Películas en la lista de aplicaciones instalables e instálalo como cualquier otro módulo de Odoo.

## Configuración

Después de instalar el módulo, es necesario configurarlo, proporcionando la URL y la clave de API del servicio externo de películas:

- En Odoo, ve al menú Ajustes.
- Busca la sección Películas en la pantalla de ajustes. Allí encontrarás los campos para configurar la URL del API de Películas y la API Key.
- Ingresa la URL base del servicio de películas (por ejemplo, https://api.ejemplo.com/movies) y la clave de API que te proporcionó el proveedor del servicio.
- Guarda la configuración.
- Opcionalmente, verifica que la tarea programada esté activa: navega a Ajustes > Técnico > Automatización > Acciones planificadas > "Importar películas desde API".

## Pruebas

\*\* Las pruebas se deben lanzar después de haber inicializado la base de datos e instalado el addon.

El módulo "Películas" incluye pruebas automatizadas y también se puede verificar manualmente su funcionamiento:

- Ejecución de pruebas automatizadas: Si deseas correr las pruebas incluidas, puedes hacerlo al instalar el módulo en un entorno de desarrollo con las pruebas habilitadas. Por ejemplo, inicia Odoo con el parámetro --test-enable. Un comando típico sería:

  ```bash
  make run-tests
  ```

  o

  ```bash
  docker compose run --rm web odoo --test-enable -d odoo -u movie_module
  ```

  Esto instalará el módulo en la base de datos especificada y ejecutará las pruebas definidas en tests/test_movie.py. Al finalizar, en la consola se mostrará un resumen de las pruebas (indicando OK si pasaron correctamente o detalles de cualquier error).

- Verificación del cron (tarea programada): Para comprobar manualmente la importación periódica de películas, asegúrate de haber configurado correctamente la URL y la API Key como se indicó. Luego, espera uno o dos minutos para dar tiempo a que el cron se ejecute (por defecto corre cada 1 minuto). A continuación, ve al menú Películas (agregado por el módulo) y verifica que aparecen registros de películas que antes no estaban, correspondientes a datos obtenidos de la API externa. También puedes revisar el registro de logs de Odoo para ver mensajes de éxito o error relacionados con la ejecución de la tarea programada.

- Prueba del endpoint REST: Para validar el endpoint /api/top_movies, puedes utilizar una herramienta como cURL o Postman. Por ejemplo, ejecuta en una terminal:

  ```bash
  curl -X GET http://localhost:8069/api/top_movies
  ```

  Deberías recibir una respuesta en formato JSON con las 10 películas de mayor ranking actualmente almacenadas (en caso de que no hayan 10 se muestran todas). Cada elemento del JSON incluirá el id de la película (en Odoo), el title (título) y el ranking. Verifica que la respuesta contenga hasta 10 elementos y que estén ordenados de mayor a menor según el ranking. Si la respuesta está vacía o no ves los datos esperados, asegúrate de que existan suficientes películas registradas y de que el módulo esté instalado/configurado correctamente.


## Changelog
- 0.1.1: [Estructura básica] --> Se implementa estructura básica del módulo personalizado.
- 0.2.1: [Módulo Péliculas] --> Se agregan modelos, vistas, etc, necesarios para el módulo.
- 0.3.1: [Cron Job] --> Se implementa tarea programada para generar películas desde servicio (API) externo.
- 0.4.1: [API Rest] --> Se disponibliza servicio para obtener top de películas ordenadas por ranking.


## Autores y licencia

Desarrollado por Osmani Casanueva (osmanicasanueva@gmail.com).
