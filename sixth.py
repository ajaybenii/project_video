from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def sixth_image(first_cover_image,connection_roads):
        
        # connection_roads = [connection_roads]

        # print("connection road = ",connection_roads[0])

        # print(len(connecting_road))
        first_cover_image = Image.open(first_cover_image).resize((1200,800))
        new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
        
        # Define color and opacity of rectangle to paste onto new image
        rectangle_color1 = (60,179,113)
        rectangle_color2 = (0, 0, 0, 180)
        rectangle_color3 = (255,255,255,50)
        
        # Paste colored rectangle onto new image
        draw = ImageDraw.Draw(new_image)

        font = ImageFont.truetype("arialbd.ttf", 25)
        font1 = ImageFont.truetype("arial.ttf", 20)

        text_color1 = (255, 255, 255)
        
        if len(connection_roads) == 2:
             
            draw.rectangle([(120, 280), ((300,450))], fill=rectangle_color1)
            draw.rectangle([(140, 300), ((650,500))], fill=rectangle_color2)
            draw.rectangle([(140, 410), ((650,410))], fill=rectangle_color3)

            draw.text((170, 320), (f"Connecting Roads"), fill=text_color1, font=font)

            draw.text((170, 370), connection_roads[0], fill=text_color1, font=font1)
            draw.text((170, 445), connection_roads[1], fill=text_color1, font=font1)

        if len(connection_roads) == 1:

        
            draw.rectangle([(130, 290), ((230,370))], fill=rectangle_color1)
            draw.rectangle([(140, 300), ((650,410))], fill=rectangle_color2)

            # draw.rectangle([(140, 410), ((650,410))], fill=rectangle_color3)

            draw.text((170, 320), (f"Connecting Road"), fill=text_color1, font=font)
            
            draw.text((170, 360), connection_roads[0], fill=text_color1, font=font1)
        
        

        output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
        # logo = Image.open("sq_logo.png").resize((150,90)).convert("RGBA")
        # output_image.paste(logo, (1050, 2), mask=logo)

        output_image.save("image6.png")
        result = "image6.png"
        # output_image.show()
        return result

# first_image(first_cover_image = "1.jpg",Connecting_road = ("Souhtern Peripheral Road - 6km","NH-8 - 10 km"))