import pyautogui as pg
from PIL import ImageGrab
import time
from PIL import Image
from pytesseract import pytesseract
import nltk
from nltk.tokenize import sent_tokenize
import keyboard, webbrowser

ind = 0
time_to_wait = 5
x_start = 0
x_end = pg.size()[0]

size_above = 150
total_height = 300

path_to_tesseract = r"C:/Users/arivuselvan.intern/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
image_path = r"image.png"

file_path = "data.txt"

def clear_file():
    with open(file_path, "w") as f:
        pass

def write_file(tokens):
    with open(file_path, "a") as f:
        for tok in tokens:
            f.write(tok)
            f.write("\n")

def analysis():
    
    freq_dict = dict()
    with open(file_path, "r") as f:
        r = f.readlines()
        l = len(r)
    unique_sentence = set(r)
    for i in unique_sentence:
        freq_dict[i] = r.count(i)
    freq_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)}
    score_dict = dict()
    
    output_file_path = "output.txt"  
    threshold_score = (100/l) * 1 

    with open(output_file_path, "w") as output_file:
        for i in freq_dict:
            score = (freq_dict[i] / l) * 100
            if score > threshold_score:
                score_dict[i] = score
                output_file.write(f"{i}{score}\n")
                print(f"{i} - score: {score}")
                
    return score_dict

if __name__=="__main__":
    clear_file()
    while(keyboard.is_pressed('q') == False):
        point = pg.position()
        i = 0
        flag = 0
        while(point==pg.position() and i<time_to_wait):
            if keyboard.is_pressed('q') == True:
                break
            time.sleep(1)
            i+=1
        if keyboard.is_pressed('q') == True:
            break
        if(i==time_to_wait):
            flag = 1
        if(flag):
            y_start = point[1] - size_above if point[1] > size_above else 0
            y_end = y_start +  total_height if(y_start < (pg.size()[1]-total_height)) else pg.size()[1]

            ss_region = (x_start, y_start, x_end, y_end)
            ss_img = ImageGrab.grab(ss_region)
            ss_img.save(image_path)
            ind += 1
            img = Image.open(image_path)
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_string(img)
            text = text.replace("\n", " ") 
            tokens = sent_tokenize(text)
            write_file(tokens)
    score_dict = analysis()
    webbrowser.open("http://127.0.0.1:5000/", new=2, autoraise=True)


    
