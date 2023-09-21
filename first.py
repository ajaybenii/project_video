from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as mp
from io import BytesIO
import numpy as np


def first_image(first_img,project_name,location,price):
    
    first_cover_image = Image.open(first_img).resize((1200,800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
    
    # Define color and opacity of rectangle to paste onto new image
    rectangle_color1 = (60,179,113)
    rectangle_color2 = (0, 0, 0, 200)
    
    
    # Paste colored rectangle onto new image
    draw = ImageDraw.Draw(new_image)
    
    draw.rectangle([(120, 480), ((300,620))], fill=rectangle_color1)
    draw.rectangle([(140, 500), ((650,650))], fill=rectangle_color2)
    
    text_color = (255, 255, 255) # white text color

    font = ImageFont.truetype("arialbd.ttf", 27)
    font1 = ImageFont.truetype("arial.ttf", 20)
    font2 = ImageFont.truetype("arialbd.ttf", 27)
    font3 = ImageFont.truetype("arialbd.ttf", 25)

    text_color1 = (255, 255, 255)
    rs_text_color =(238,130,238) 

    draw.text((170, 540), (f"{project_name}"), fill=text_color1, font=font)
    draw.text((200, 590), (f"{location}"), fill=text_color, font=font1)
    # draw.text((170, 640), (f"Rs {price}"), fill=rs_text_color, font=font2)

    # draw.text((60, 550), (f"Square feet     {area}sq.ft"), fill=text_color1, font=font1)    
    text_color = (255, 255, 255) # white text color
    font = ImageFont.truetype("arialbd.ttf", 20) # define font and font size

    output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
    # logo = Image.open("sq_logo.png").resize((150,90)).convert("RGBA")
    # output_image.paste(logo, (1050, 2), mask=logo)

    # bedroom = Image.open("b1.png").resize((50,50)).convert("RGBA")
    # output_image.paste(bedroom, (50, 450), mask=bedroom)
    # output_image.save(str(f"{i}.png"))

    location_logo = Image.open("location.png").resize((20,20)).convert("RGBA")
    output_image.paste(location_logo, (170,590), mask=location_logo)

    output_image.save("image1.png")
    result = "image1.png"
    # output_image.show()
    first_cover_image = Image.open(result).resize((1200,800))

    return result

