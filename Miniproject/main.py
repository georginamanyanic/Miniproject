
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import re
import numpy as np
from src.scrapping import *
import src.cleaning 

ingredientes_bonpreu = ['https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=b4098292-6a2a-428f-ace6-076a19878890',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=22a85cdc-fce2-4818-adad-9bd150c0a38d',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=8d28608c-a0b0-4fe5-8104-e906f732365c',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=71f75f2f-0352-4035-8e6e-329727bb2167',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=28fde871-8fb9-4f23-a386-ae6c8d64a149',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=a8be0b30-ea43-431a-af01-5defaa0072b7',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=1a5c3d3d-7f00-48ef-bb8e-ff26aad9e89c',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=7f1b40c8-35e4-44b5-b07a-eb878b788c17',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=7d568dd6-2e26-4f25-8149-c67f3f0e33a5',
                        'https://www.compraonline.bonpreuesclat.cat/products?sortBy=favorite&sublocationId=7a425422-8ca4-45f1-8294-29fa0deafcef']

ingredientes_bonarea = ['https://www.bonarea-online.com/categorias/ternera/13_300_010_070', 
                        'https://www.bonarea-online.com/categorias/verdura/13_300_060_020', 
                        'https://www.bonarea-online.com/categorias/aceite-de-oliva/13_300_110_020_010',
                        'https://www.bonarea-online.com/categorias/sal/13_300_110_030', 
                        'https://www.bonarea-online.com/categorias/harina/13_300_140_020_010',
                        'https://www.bonarea-online.com/categorias/pasta/13_300_140_030',
                        'https://www.bonarea-online.com/categorias/lacteos-y-derivados/13_300_080_010',
                        'https://www.bonarea-online.com/categorias/nata-mantequilla-y-margarina/13_300_080_030',
                        'https://www.bonarea-online.com/categorias/base-de-tomate-y-ketchup/13_300_150_020']

ingredientes_dia = ['https://www.dia.es/compra-online/despensa/salsas/tomate/cf', 
                    'https://www.dia.es/compra-online/despensa/lacteos-y-huevos/leche/cf',
                    'https://www.dia.es/compra-online/frescos/carne/mixto/cf', 
                    'https://www.dia.es/compra-online/despensa/pastas-harinas-y-masas/pastas/cf/tipo+canelones-y-lasana',
                    'https://www.dia.es/compra-online/despensa/pastas-harinas-y-masas/harinas-y-levaduras/cf/producto+harina',
                    'https://www.dia.es/compra-online/despensa/aceites-vinagres-y-alinos/aceites/cf/producto+aceite-de-oliva',
                    'https://www.dia.es/compra-online/frescos/charcuteria-y-quesos/quesos/cf/corte+rallado',
                    'https://www.dia.es/compra-online/despensa/lacteos-y-huevos/mantequilla-y-margarina/cf/producto+mantequilla',
                    'https://www.dia.es/compra-online/frescos/verduras-y-hortalizas/ajos-cebollas-y-puerros/cf',
                    'https://www.dia.es/compra-online/despensa/sal-y-especias/cf/producto+sal']

from src.scrapping import *
df_bonpreu = df_supermercados(ingredientes_bonpreu)
print(df_bonpreu)