import requests
import json
import os
import logging

def caption(image_path):
        # Replace <Subscription Key> with your valid subscription key.
    subscription_key = "Your API Key"
    assert subscription_key
    vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/"

    analyze_url = vision_base_url + "analyze"
    # Set image_path to the local path of an image that you want to analyze.
    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                  'Content-Type': 'application/octet-stream'}
    params     = {'visualFeatures': 'Categories,Tags,Description,Color,ImageType'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    analysis = response.json()
    caption = analysis['description']['captions'][0]['text']
    return caption