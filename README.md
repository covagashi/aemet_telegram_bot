# Bot Telegram

Este es un proyecto python el cual te dice el tiempo que hace cada mañana, también puedes activarlo manualmente.

## Comandos disponibles

Los comandos disponibles de momento son:

- start: Da un mensaje de bienvenida
- weather: Se conecta a AEMET y descarga la previsión meteorológica
- hello: Te saluda

## Tareas periódicas

Las tareas que se ejecutan periódicamente son las siguientes:
Se ejecuta cada día a las 7 AM para decirte el tiempo.
(Al hacer el deploy en Heroku puede que  entre en modo reposo)

## Configuración en los archivos en vuestro github privado

Es necesaria la edición del fichero **config.py**:

```
TELEGRAM_TOKEN = "AAAA"
TELEGRAM_GROUP_ID = 12345
WAIT_TIME_SECONDS_WEATHER = 3600
AEMET_TOKEN = "BBBBB"
CITY_ID = "03333"
```
Solo es necesario en telegram token, aement token y el city ID, el resto se puede dejar tal cual.

Este Bot está preparado para ser alojado en Heroku, simplemente hay que crear una app en heroku y pegar el enlace
en bot.py donde en la línea del código que se puede ver debajo.

```
  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=bot_token)
    updater.bot.setWebhook('YOUR NAME APP HERE' + bot_token)
    updater.idle()
```

## Configuración Heroku

Heroku es una nube donde puedes tener apps gratis con cierta limitaciones. Para este bot es mas que suficiente.

- Creamos la cuenta de Heroku
- creamos la App, recordad que este es el nombre para modificar en **updater.bot.setWebhook('YOUR NAME APP HERE' + bot_token)**
![Alt text](https://i.imgur.com/5otmEk4.jpg)

- Conectamos nuestro github y buscamos el repositorio privado
![Alt text](https://i.imgur.com/gvpF723.jpg)

- Bajamos abajo del todo y le damos al deploy manual
![Alt text](https://i.imgur.com/iVqGi7n.jpg)

- Ahora entrais en telegram y hablais con vuestro bot. Ya lo teneis!

