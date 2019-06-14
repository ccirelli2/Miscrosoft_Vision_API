# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:55:07 2019

@author: Chris.Cirelli
"""

'''REFERENCES------------------------------------------------------------------

Documentation:    https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/
Read API:         Most advanced model that they currently have. 
                  https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/587f2c6a154055056008f200

Github Repos - Python & Vision API
                    https://github.com/Microsoft/Cognitive-Vision-Python

'''


'''KEYS------------------------------------------------------------------------

'''





########### Python Example #############
import os
import json
import requests

API_KEY = '6db2a65139624185bec2bb99b3997b68'
ENDPOINT = 'https://YOUR_ENDPOINT_REGION.api.cognitive.microsoft.com/vision/v1.0/ocr'
DIR = 'YOUR_PATH_TO_IMAGE_FILES'

def handler():
    text = ''
    for filename in sorted(os.listdir(DIR)):
        if filename.endswith(".jpeg"): 
            pathToImage = '{0}/{1}'.format(DIR, filename)
            results = get_text(pathToImage)
            text += parse_text(results)

    open('output.txt', 'w').write(text)

def parse_text(results):
    text = ''
    for region in results['regions']:
        for line in region['lines']:
            for word in line['words']:
                text += word['text'] + ' '
            text += '\n'
    return text  

def get_text(pathToImage):
    print('Processing: ' + pathToImage)
    headers  = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params   = {
        'language': 'en',
        'detectOrientation ': 'true'
    }
    payload = open(pathToImage, 'rb').read()
    response = requests.post(ENDPOINT, headers=headers, params=params, data=payload)
    results = json.loads(response.content)
    return results

if __name__ == '__main__':
    handler()





















