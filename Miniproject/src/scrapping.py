import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import re
import numpy as np

"""Las funciones de scrapping se usan para extraer 
los datos de urls, en este caso obterner los precios_unidad, caracteristicas, precios_kg_l, cantidad de producto y link.
Guardo los datos en un diccionario para convertirlo a DataFrame.
Argumentos: i - link de página web de donde se extrae el código html y parsea
Return: df - DataFrame donde los datos mencionados anteriormente son las columnas """

def scrapping_dia (i): 
        
        html = requests.get(i) 
        soup = BeautifulSoup(html.content, "html.parser")
        
        precio_unidad = [float(i.getText().strip().replace(',','.')[0:4]) for i in soup.find_all('p',{'class':'price'})]
        caracteristicas = [i.getText().strip() for i in soup.find_all('span',{'class':'details'})]
        precio_kg_l = [float(i.getText().strip().replace(',','.')[0:4]) for i in soup.find_all('p',{'class':'pricePerKilogram'})]
        link = ['https://www.dia.es/'+ i.find('a').get('href') for i in soup.find_all('div',{'class':'product-list__item'})]
        cantidad_producto = [round(precio_unidad[i]/precio_kg_l[i],1) for i in range(len(precio_unidad))]
    
        dict_ = {'precio_unidad':precio_unidad, 'caracteristicas':caracteristicas, 'precio_kg_l':precio_kg_l,'cantidad_producto': cantidad_producto, 'link': link}
    
        df = pd.DataFrame (dict_)
        
        return df

def scrapping_bonpreu (url):
    html = requests.get(url) 
    soup = BeautifulSoup(html.content, "html.parser")
    
    caracteristicas = [i.find('a').getText().strip() for i in soup.find_all('h3',{'class':'text__Text-sc-6l1yjp-0 iWlLMY'})]
    precio_unidad = [float(i.getText().strip().replace(',','.')[0:3]) for i in soup.find_all('strong',{'class':'base__Price-sc-1mnb0pd-29 sc-jRQAMF iDLLj hFlPaZ'})]
    
    precio1_pre = [i.getText().strip().replace(',','.') for i in soup.find_all('span',{'class':'text__Text-sc-6l1yjp-0 standard-promotion__PromotionIntentText-sc-1vpsrpe-2 fop__PricePerText-sc-1e1rsqo-3 dLNLFE jVJmKC eJshgd'})]
    precio_kg_l = [float(re.search(r'\d+\.\d+', i).group()) for i in precio1_pre]
    link = ['https://www.compraonline.bonpreuesclat.cat/' + i.find('a').get('href') for i in soup.find_all('h3',{'class':'text__Text-sc-6l1yjp-0 iWlLMY'})]
    cantidad_producto = [round (precio_unidad[i]/precio_kg_l[i],3) for i in range(len(precio_unidad))]

    dict_ = {'precio_unidad':precio_unidad, 'caracteristicas':caracteristicas, 'precio_kg_l':precio_kg_l, 'cantidad_producto': cantidad_producto, 'link':link}
    
    
    return pd.DataFrame(dict_)

def scrapping_bonarea (url): 
    html = requests.get(url) 
    soup = BeautifulSoup(html.content, "html.parser")
    
    precios_pre = [i.getText().split() for i in soup.find_all('div',{'class':'price'})]
    precio_unidad = [float(sublista[0].replace(',','.')) for sublista in precios_pre]
    precio_kg_l = [float(sublista[2].replace(',','.').replace('(','')) for sublista in precios_pre]
    caracteristicas = [i.getText() for i in soup.find_all('div',{'class':'text'})]
    cantidad_producto = [round (precio_unidad[i]/precio_kg_l[i],1) for i in range(len(precio_unidad))]
    
    dict_ = {'precio_unidad':precio_unidad, 'caracteristicas':caracteristicas, 'precio_kg_l':precio_kg_l, 'cantidad_producto': cantidad_producto}
    
    return pd.DataFrame (dict_)


def df_supermercados (list_ingredientes):

    """La función toma como argumento una lista en la que se itera por cada link, identifica de
     que supermercado es, llama a la función de scrapping correspondiente, crea un dataframe de un producto en concreto. Para 
      no sobrescribir los dataframes, creo un dataframe general vacío (df_super) en el que concatenar los df_producto allí. 
       Argumentos: list_ingredientes - lista de los links de los productos para cada supermercado
       Return: df_super - Dataframe que contiene todos los productos """
   
    df_super = pd.DataFrame () # creo un data frame vacio donde concatenaré para cada producto

    for i in list_ingredientes: #loop de la lista ingredientes para cada super, cada link es la categoria del ingrediente
            
        if 'bonpreu' in i:
            df_producto = scrapping_bonpreu(i)
            df_super = pd.concat([df_producto, df_super], ignore_index=True)
            
    
        if 'dia' in i: 
            df_producto = scrapping_dia(i)
            df_super = pd.concat([df_producto, df_super], ignore_index=True)
        
        if 'bonarea' in i:
            df_producto = scrapping_bonarea(i)
            df_super = pd.concat([df_producto, df_super], ignore_index=True)
            
            

    return df_super

