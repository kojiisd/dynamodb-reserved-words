import sys
import os


sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib'))
from bs4 import BeautifulSoup
import requests

URL = os.environ['TARGET_URL']

def run(event, context):
    
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    
    result_tmp = soup.find("code")
    if result_tmp == None:
        return "No parsing target"
    
    result = result_tmp.string

    return result.split('\n');
