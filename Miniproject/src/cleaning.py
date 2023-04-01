import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import re
import numpy as np
import src.scrapping as cl

#Supermercado Bonarea

def scrapping_quesos_bonarea(url):
    """Esta función solamente es para Bonarea dado que hay dos productos en la categoría queso
    que no contienen el precio/kg y me daba error ya que las arrays no tenian el mismo len. Por lo que decidio omitir estos 
    dos productos para mi análisi. Tiene un format parecido a las funciones scrapping, con la diferencia que 
    aqui concatena el dataframe de quesos con el dataframe de todos los productos. """
   
    html = requests.get('https://www.bonarea-online.com/categorias/rallados/13_300_050_050?order=3') 
    soup = BeautifulSoup(html.content, "html.parser")
    
    precios = [i.getText().split() for i in soup.find_all('div',{'class':'price'})][0:10]
    
    
    precio_unidad = [float(sublista[0].replace(',','.').replace('€','')) for sublista in precios]
    precio_kg_l = [float(sublista[2].replace(',','.').replace('(','')) for sublista in precios]
    caracteristicas = [i.getText() for i in soup.find_all('div',{'class':'text'})][0:10]
    cantidad_producto = [round (precio_unidad[i]/precio_kg_l[i],1) for i in range(len(precio_unidad))]

    
    dict_ = {'precio_unidad':precio_unidad, 'caracteristicas':caracteristicas, 'precio_kg_l':precio_kg_l, 'cantidad_producto': cantidad_producto}
    
    df_bonarea_quesos = pd.DataFrame (dict_)
    df_bonarea = pd.concat([cl.df_supermercados(ingredientes_bonnarea), df_bonarea_quesos], ignore_index=True)
    
    return df_bonarea

