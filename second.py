from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def second_image(second_img,units,Configuration):
    
    first_cover_image = Image.open(second_img).resize((1200,800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
    
    # Define color and opacity of rectangle to paste onto new image
    rectangle_color1 = (60,179,113)
    rectangle_color2 = (0, 0, 0, 180)
    rectangle_color3 = (255,255,255,50)
    
    
    # Paste colored rectangle onto new image
    draw = ImageDraw.Draw(new_image)
    
    draw.rectangle([(120, 280), ((300,450))], fill=rectangle_color1)
    draw.rectangle([(140, 300), ((650,520))], fill=rectangle_color2)
    draw.rectangle([(140, 410), ((650,410))], fill=rectangle_color3)
    
    text_color = (255, 255, 255) # white text color

    font = ImageFont.truetype("arialbd.ttf", 25)
    font1 = ImageFont.truetype("arial.ttf", 20)
    font2 = ImageFont.truetype("arialbd.ttf", 27)
    font3 = ImageFont.truetype("arialbd.ttf", 25)

    text_color1 = (255, 255, 255)
    rs_text_color =(238,130,238) 
    draw.text((170, 320), (f"Project Size"), fill=text_color1, font=font)
    draw.text((170, 365), (f"{units} units"), fill=text_color1, font=font1)
    draw.text((170, 420), (f"Configuration"), fill=text_color, font=font)
    draw.text((170, 460), (f"{Configuration}"), fill=text_color1, font=font1)
    
    
    text_color = (255, 255, 255) # white text color
    font = ImageFont.truetype("arialbd.ttf", 20) # define font and font size

    output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)

    output_image.save("image2.png")
    result = "image2.png"
    # output_image.show()
    return result

# second_image(first_cover_image = "1.jpg",units = "1320",Configuration = "3,4 BHK Flat from Sq.ft to 2635 Sq.ft.")