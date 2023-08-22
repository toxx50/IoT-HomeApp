from datetime import datetime
import PIL


# MAIN FRAME

MAIN_FRM_CLR = 'white'

# HOME FRAME

HOME_CLR = '#00BE9E'

# OPTIONS FRAME

OPT_FONT = ('Bahnschrift Bold', 15)

CLOTH_CLR = 'light grey'

# WEATHER API

URL = 'https://weather.com/hr-HR/weather/today/l/539ed99ddac6f415b6518f1f3cc8386d27a9ae5baa5039ed29094c58c447d3dc'

#FILES PATH
CLOUD_PATH = "C:/Users/Korisnik/PycharmProjects/IoT-HomeApp/files_img/weather-forecasting.png"
CLOTH_PATH = "C:/Users/Korisnik/PycharmProjects/IoT-HomeApp/files_img/545546.png"


"""OVISNO O VREMENU DA LI JE DAN ILI NOĆ, BITI ĆE TAMNA ILI SVIJETLA BOJA POZADINA U WEATHER TABU"""
now = datetime.now()
current_time = now.strftime('%H')
if int(current_time)>6 and int(current_time)<20:
    LABEL_CLR = '#01AFFB'
else:
    LABEL_CLR = '#222454'






