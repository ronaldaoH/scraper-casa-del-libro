
import requests
import lxml
import pprint
from bs4 import BeautifulSoup
import extruct

from w3lib.html import get_base_url
def extraer_informacion_web():
    pp = pprint.PrettyPrinter(indent=2)
    r = requests.get('https://www.casadellibro.com/libro-los-renglones-torcidos-de-hollywood/9788412094749/11187413')

    base_url = get_base_url(r.text, r.url)
    data = extruct.extract(r.text, base_url=base_url)

    schema = data['json-ld']

    soup = BeautifulSoup(r.text, 'lxml')

    imagen = soup.find('img', {'class' : 'product-image'})

    descripcion = soup.find('div', {'class' : 'hidden-sm-and-down'})
    desc = descripcion.text

    desc = desc.replace("Ver más",'').strip()

    if "CRÍTICAS" in desc:
        desc = desc.split("CRÍTICAS")
        desc = desc[0]
    if "Resumen" in desc:
        desc = desc.split("Resumen")
        desc = desc[1]
    obj =  {}
    obj['desc'] = desc
    obj['imagen'] = imagen['data-src']
    obj['schema'] = schema
    print (obj)
    print (type(obj))

extraer_informacion_web()
