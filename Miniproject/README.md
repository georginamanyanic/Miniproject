# Miniproyecto - Webscrapping
La idea inicial del proyecto era realizar un comparador de precios de supermercados mediante web scrapping. Dado la limitación de tiempo para llevarlo a cabo, he reducido el alcance a 3 supermercados (Bonpreu, Bonarea o Dia) y he seleccionado unos productos específicos necesarios para una receta, por lo que ha sido un webscrapping estático mediante el uso de la librería BeautifulSoup. 
El objetivo de este proyecto es saber en qué supermercado me sale más barata la compra de los ingredientes para hacer unos canelones. Los ingredientes y cantidades de la receta se encuentran en el siguiente diccionario: 

dict_receta = {'preparado mixto carne' : 0.5, 'tomate' : 0.1, 'harina': 0.1, 'mantequilla':0.1, 'leche': 1, 'cebolla': 0.2, 'ajo':0.06, 'pasta': 0.25, 'quesos': 0.250, 'aceite': 0.06, 'sal': 0.015}

## Extracción de datos
Para la extracción de datos, he usado la librería request que permite realizar las peticiones a la página web y la librería BeautifulSoup que nos permite extraer los datos de html y parsearlos para transformar el documento html o xml en un árbol de objetos de Python. Para ello, he creado el `scrapping.py` que extrae de cada supermercado los siguientes datos de los productos y lo transforma a DataFrame mediante la librería pandas: 
-	Precio/unidad
-	Precio/kg o Precio/L
-	Características
-	Link
-	Cantidad/unidad

Para realizar esta extracción he seguido los siguientes pasos:
1.	Crear una lista para cada supermercado que contiene los links de las categorías de los productos 
2.	Definir una función para extraer los datos mencionados anteriormente y transformarlos a DataFrame para cada supermercado usando BeautifulSoup y requests
3.	Definir una única función que toma como atributo la lista de links. Esta función itera por los valores de la lista, identifica de qué supermercado es el link, llama a la función de scrapping del supermercado y concatena los dataframes de cada producto en un dataframe vacío. 

De esta forma, obtengo un dataframe para cada supermercado que contiene la información de los productos que me interesan. 

## Data cleaning
Para el proceso de limpieza de los dataframes, he creado el `cleaning.py` que efectúa lo siguiente: 
1.	Crear una nueva columna que indica que tipo de producto es (el mismo que las keys del dict_receta) a partir de las columnas características y link. 
2.	Dropear los nan values de la columna nueva columna tipo.


Además, para precisar cuantas unidades de producto se tienen que comprar teniendo en cuenta la cantidad de producto que se necesita para la receta, he creado las siguientes columnas: 
1.	Columna cantidad_receta: cantidad de producto necesario para la receta. He usado la función map en el diccionario dict_receta aplicandolo a la columna tipo, por lo que en cada valor de la columna tipo, la función map busca en el diccionario el valor correspondiente y lo asigna a la nueva columna. 
2.	Columna unidades: cuantas unidades de producto debo comprar teniendo en cuenta lo que necesito para la receta (división de cantidad_receta y cantidad_producto). Los valores eran floats, por lo que he aplicado una función a la columna que los devuelva a enteros usando la lógica de que por ejemplo si el valor es 1.5 unidades devuelva 2.
3.	Columna coste: el precio a pagar según el número de unidades que debes comprar de producto. (precio_unidad * unidades)

## Análisis  y resultado
Para saber en qué supermercado la compra es más barata, he creado tres subdataframes agrupando los productos por tipo, usando la función idxmin para obtener el índice del producto con un coste más bajo. Por último, he agregado una última fila que corresponde al total sumando los valores de la columna coste. 
El resultado final del proyecto es que el supermercado más barato es el Bonpreu con una compra de 17.1 euros. Mientras que en Dia la compra sube a 19 euros y en el Bonarea sale a 21.6 euros. 

