import numpy as np
import pandas as pd
import easyocr
import matplotlib.pyplot as plt
reader = easyocr.Reader(['en'])
import cv2
from PIL import Image
import pytesseract
import re
from pyzbar.pyzbar import decode




def BarcodeReader(file_name):
  result = []
  path = f'C:/Users/dwoic/docReader/img/{file_name}'
  img = cv2.imread(path)
  detectedBarcodes = decode(img)

  if not detectedBarcodes:
    gamma_img = adjust_gamma(img, 0.5)
    gamma_read = Image.fromarray(gamma_img)
    # im.save('gamma_'+file_name)
    # gamma_read = cv2.imread('C:/Users/dwoic/OneDrive/Рабочий стол/Практика/dataset/'+file_name)
    gamma_barcodes = decode(gamma_read)
    for barcode in gamma_barcodes:
      if barcode.data!="":
        result.append(barcode.data)
        result.append(barcode.type)
  else:
    for barcode in detectedBarcodes:
      if barcode.data!="":
        result.append(barcode.data)
        result.append(barcode.type)
  return result

def adjust_gamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)






def getNumberDoc(fileName):
  image, bolean = getRectangleOnNum(fileName)

  if (bolean):
    heightImg, widthImg, channels = image.shape
    image = image[int(heightImg / 2):heightImg - 10, 10:int(widthImg / 2) - 15]
    return checkDocNum(image)
  else:
    image, bolean = getRectangleOnNum(fileName, True)
    if (bolean):
      heightImg, widthImg, channels = image.shape
      image = image[int(heightImg / 2):heightImg - 10, 10:int(widthImg / 2) - 15]
      return checkDocNum(image)
  return None




def getRectangleOnNum(fileName, bolean=False):
    print(f"C:/Users/dwoic/docReader/{fileName}")
    image = cv2.imread(f"C:/Users/dwoic/docReader/img/{fileName}")

    heightImg, widthImg, channels = image.shape
    if (heightImg < widthImg):
      image = image[int(heightImg / 2 - 1000):int(heightImg / 2 - 200), int(widthImg / 2 - 700):int(widthImg / 2 + 700)]
    else:
      image = image[:, int(widthImg / 2 - 550):int(widthImg / 2 + 550)]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Размытие
    if (bolean):
      gray = cv2.GaussianBlur(gray, (13, 13), 0)
      gray = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)[1]
    else:
      gray = cv2.GaussianBlur(gray, (3, 3), 0)
    # Распознавание контуров
    edged = cv2.Canny(gray, 10, 250)

    # Закрытие открытых контуров
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    # Нахождение контуров в изображении
    contours, _ = cv2.findContours(closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    total = 0

    image_result = image.copy()

    # Перебор контуров
    for c in contours:
      # Аппроксимирование (сглаживание) контура
      peri = cv2.arcLength(c, True)
      approx = cv2.approxPolyDP(c, 0.05 * peri, True)

      # Если у контура 6 вершины, предполагаем, что это нужная нам кнопка
      if len(approx) != 4:
        continue

      # Дополнительно фильтруем по размеру
      rect = cv2.boundingRect(c)
      width, height = rect[2:]

      absWidth = widthImg / width
      absHeight = heightImg / height

      # Нужно подбирать
      if (widthImg > heightImg):
        if (height < 130 or width < 850) or width > 1200 or height > 200:
          continue
      else:
        if absHeight > 60 or absHeight < 30 or absWidth > 6.5 or absWidth < 3:
          continue

      cv2.drawContours(image_result, [approx], -1, (0, 0, 255), 4)
      image = image[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]

      return [image, True]

    return [None, False]




def checkDocNum(img):
    string = reader.readtext(img)
    if (string):
      stringRet = string[0][1]
      if (stringRet[0] != '6'):
        stringRet = '6' + stringRet[1:]
      stringRet = stringRet.replace('+', '1')
      stringRet = stringRet.replace(':', '')
      stringRet = stringRet.replace(' ', '1')
      stringRet = stringRet.replace(',', '1')
      stringRet = stringRet.replace('[', '7')
      if (len(stringRet) > 9):
        stringRet = stringRet[:10]

      return stringRet
    else:
      return None


def getDocInfo(fileName):
  number = getNumberDoc(fileName)
  barcode, codeType = BarcodeReader(fileName)
  return {'number': number, 'barcode': barcode, 'codeType': codeType}


