from PIL import Image, ImageDraw, ImageFont

def third_image(first_cover_image, priceList):
    first_cover_image = Image.open(first_cover_image).resize((1200, 800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))

    # Define color and opacity of rectangle to paste onto new image
    rectangle_color1 = (60, 179, 113)
    rectangle_color2 = (0, 0, 0, 180)
    rectangle_color3 = (255, 255, 255, 50)

    # Paste colored rectangle onto new image
    draw = ImageDraw.Draw(new_image)

    if (len(priceList)) == 3:
        
        draw.rectangle([(120, 280), (300, 450)], fill=rectangle_color1)  # Green Rectangle
        draw.rectangle([(140, 300), (850, 750)], fill=rectangle_color2)  # Large Rectangle
        
        # Horizontal Lines
        for y in range(380, 851, 85):
            draw.rectangle([(180, y), (800, y)], fill=rectangle_color3)

        # Vertical Lines
        draw.rectangle([(180, 380), (180, 720)], fill=rectangle_color3)
        draw.rectangle([(800, 380), (800, 720)], fill=rectangle_color3)


    if (len(priceList)) == 2:

        draw.rectangle([(120, 280), (300, 450)], fill=rectangle_color1)  # Green Rectangle
        draw.rectangle([(140, 300), (850, 650)], fill=rectangle_color2)  # Large Rectangle
        
        # Horizontal Lines
        for y in range(380, 851, 85):

            draw.rectangle([(180, y), (800, y)], fill=rectangle_color3)
            
            if y ==635:
                break
        # Vertical Lines
        draw.rectangle([(180, 380), (180, 635)], fill=rectangle_color3)#LEFT line
        draw.rectangle([(800, 380), (800, 635)], fill=rectangle_color3)#Right Line

    if (len(priceList)) == 1:

        draw.rectangle([(120, 280), (300, 450)], fill=rectangle_color1)  # Green Rectangle
        draw.rectangle([(140, 300), (850, 580)], fill=rectangle_color2)  # Large Rectangle
        
        # Horizontal Lines
        for y in range(380, 851, 85):

            draw.rectangle([(180, y), (800, y)], fill=rectangle_color3)
            
            if y ==550:
                break

        # Vertical Lines
        draw.rectangle([(180, 380), (180, 550)], fill=rectangle_color3)#LEFT line
        draw.rectangle([(800, 380), (800, 550)], fill=rectangle_color3)#Right Line


    text_color1 = (255, 255, 255)
    font1 = ImageFont.truetype("arialbd.ttf", 20)
    font2 = ImageFont.truetype("arialbd.ttf", 27)

    draw.text((160, 315), ("Unit Plans"), fill=text_color1, font=font2)
    draw.text((190, 410), ("    Unit Type                      Area               "),fill=text_color1,font=font1)
    draw.text((630,400),("New Home\nPrice*"), fill=text_color1,font=font1)

    text_color = (255, 255, 255)
    font1 = ImageFont.truetype("arialbd.ttf", 17)


    for i, data in enumerate(priceList):
        
        draw.text((200, 500 + i * 85), (data["unitType"]), fill=text_color, font=font1)
        draw.text((400, 500 + i * 85), (data["area"]), fill=text_color, font=font1)
        draw.text((630, 500 + i * 85), (data["price"]), fill=text_color, font=font1)

    output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
    output_image.save("image3.png")
    # output_image.show()
    result = "image3.png"
    return result

# Sample data you provided

# priceList = [
    # {
    #     "unitType": "2 BHK Apartment",
    #     "area": "1150 Sq. Ft.(Saleable)",
    #     "price": "Price on Request"
    # },
    # {
    #     "unitType": "3 BHK Apartment",
    #     "area": "1425 Sq. Ft.(Saleable)",
    #     "price": "Price on Request"
    # },
    # {
    #     "unitType": "3 BHK Apartment",
    #     "area": "1710 Sq. Ft.(Saleable)",
    #     "price": "Price on Request"
    # }
# ]


# third_image("1.png", priceList)
