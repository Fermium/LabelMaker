import pdfkit
import numpy as np
import pandas as pd
from jinja2 import Template
import os

template = Template(open('template.html','r').read())
data = pd.read_csv('prods.csv',header=0)
try:
    os.mkdir('tmp')
except Exception as e:
    True

try:
    os.mkdir('output')
except Exception as e:
    True

for i in range(len(data.index)):
    tmpl = template.render(
        sku=data.loc[i,'sku'],
        serial=data.loc[i,'serial'],
        test_date=data.loc[i,'test_date'])
    options = {
    "page-width":"57mm",
    "page-height":"32mm"
    }
    pdfkit.from_string(
        tmpl,
        os.path.join('tmp',str(data.loc[i,'sku'])+'.pdf'),options)
    os.system("pdftk tmp/"+str(data.loc[i,'sku'])+".pdf cat 1 output output/"+str(data.loc[i,'sku'])+'.pdf')
