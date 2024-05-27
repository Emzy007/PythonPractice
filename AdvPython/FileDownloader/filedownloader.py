# Dowloading a sample PDF file from internet

import os
'''
six.moves.urllib.request` as `u`: This is a part of the `six` library, which helps write code that is compatible with
 both Python 2 and Python 3. The `six.moves` module simplifies importing functions and modules that have different 
 locations in Python 2 and 3. Here, it imports the `urllib.request` module, which handles opening URLs. 
 '''
import six.moves.urllib.request as GetURL

def download_file_here():
    url = "https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf"
    filename = os.path.basename(url)
    print(filename)
    GetURL.urlretrieve(url,filename)
