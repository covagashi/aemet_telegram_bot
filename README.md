# Bot Telegram

Este es un proyecto python el cual te dice el tiempo que hace cada mañana, tambien puedes activarlo manualmente.

## Comandos disponibles

Los comandos disponibles de momento son:

- start: Da un mensaje de bienvenida
- weather: Se conecta a AEMET y descarga la previsión meteorológica
- hello: Te saluda

## Tareas periódicas

Las tareas que se ejecutan periódicamente son las siguientes:
Se ejecuta cada día a las 7 AM para decirte el tiempo.



## Configuración

Es necesaria la edición del fichero **config.py**:

```
TELEGRAM_TOKEN = "AAAA"
TELEGRAM_GROUP_ID = 12345
WAIT_TIME_SECONDS_WEATHER = 3600
AEMET_TOKEN = "BBBBB"
CITY_ID = "03333"
```

Solo es necesario en telegram token, aement token y el city ID, el resto se puede dejar tal cual.

## Heroku

Este Bot está preparado para ser alojado en Heroku, simplemente hay que crear una app en heroku y pegar el enlace
en bot.py donde en la línea del código que se puede ver debajo.

```
  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=bot_token)
    updater.bot.setWebhook('YOUR NAME APP HERE' + bot_token)
    updater.idle()
```


También teneis que activar el token del bot para que funcione para webook.

## Futuras implementaciones

-Busqueda de municipios por chat.
-Tiempo por horas no por día.
-Tiempo diario del día siguiente
-Poner horas para enviar el mensaje automático.
