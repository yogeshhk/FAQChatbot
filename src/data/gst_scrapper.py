# -*- coding: utf-8 -*-
# Ref: http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/

import requests
import pandas as pd
from bs4 import BeautifulSoup
    
class HTMLTableParser:
       
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return [self.parse_html_table(table) for table in soup.find_all('table') if table.has_attr('id')]  
    
    def parse_html_table(self, table):
        n_columns = 3 # hardcoded
        rows = table.find_all('tr')
        n_rows= len(rows)
        
        header_row = rows[0]
        column_names = [col.get_text() for col in header_row.find_all('td')]
        
        df = pd.DataFrame(columns = column_names,index= range(0,n_rows))

        for i in range(1,n_rows):
             row_values = [col.get_text() for col in rows[i].find_all('td')] 
             if len(row_values) <3:
                 continue
             
             question_text = row_values[1]
             answer_text = row_values[2]
             answer_text = answer_text.splitlines()[0]
             if len(answer_text) > 10:
                 answer_text = answer_text.split(' ', 1)[1]
                 
             df.iloc[i-1,0] = question_text
             df.iloc[i-1,1] = answer_text
             
        return df

if __name__ == "__main__":
    hp = HTMLTableParser()
    url = "https://cbec-gst.gov.in/faq.html"
    tables = hp.parse_url(url)
    total_df = pd.concat(tables, axis=0)
    total_df.to_csv("scrapedfaq.csv",index=False)
