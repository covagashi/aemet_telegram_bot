# Bot Telegram

Este es un proyecto python con el código para interactuar con un bot de telegram

## Comandos disponibles

Los comandos disponibles de momento son:

- add: Suma números separados por espacio
- start: Da un mensaje de bienvenida
- hello: Saluda al usuario por su nombre
- weather: Se conecta a AEMET y descarga la previsión meteorológica

## Tareas periódicas

Las tareas que se ejecutan periódicamente son las siguientes:
Se ejecuta cada día a las 7 AM

- weather

## Configuración

Es necesaria la creación de un fichero **config.py** con los siguientes datos:

```
TELEGRAM_TOKEN = "AAAA"
TELEGRAM_GROUP_ID = 12345
WAIT_TIME_SECONDS_WEATHER = 3600
AEMET_TOKEN = "BBBBB"
CITY_ID = "03333"
```


## Adaptación heroku

Nuevo archivo creado, Procfile.

El main.py se ha cambiado el nombre a bot.py
se han añadido las siguientes lineas de codigo a bot.py

```
import os
PORT = int(os.environ.get("PORT", "8443"))
```
Se reemplaza ```updater.start_polling()``` por
```
  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=bot_token)
    updater.bot.setWebhook('https://aemet-b-tele.herokuapp.com/' + bot_token)
    updater.idle()
```



