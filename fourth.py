from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


def fourth_image(first_cover_image,projectAmenities):
    
    first_cover_image = Image.open(first_cover_image).resize((1200,800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
    
    # Define color and opacity of rectangle to paste onto new image
    rectangle_color1 = (60,179,113)
    rectangle_color2 = (0, 0, 0, 180)
    rectangle_color3 = (255,255,255,50)
    
    # print("Length = ",len(amenities))

    draw = ImageDraw.Draw(new_image)     
    draw.rectangle([(10, 10), ((150,150))], fill=rectangle_color1) # Green Rectangle
    gold_color = (255,215,0)
    text_color = (255, 255, 255) # White text color

    font = ImageFont.truetype("arialbd.ttf", 20)
    font1 = ImageFont.truetype("arialbd.ttf", 20)
    font2 = ImageFont.truetype("arialbd.ttf", 23)
    font3 = ImageFont.truetype("arialbd.ttf", 18)

    text_color1 = (255, 255, 255)
    rs_text_color = (238,130,238) 
    
    
    if len(projectAmenities) == 5:
        
        draw.rectangle([(20, 20), ((600,780))], fill=rectangle_color2) # Large Rectangle

        draw.rectangle([(20, 190), ((600,190))], fill=rectangle_color3)
        draw.rectangle([(20, 330), ((600,330))], fill=rectangle_color3)
        draw.rectangle([(20, 480), ((600,480))], fill=rectangle_color3)
        draw.rectangle([(20, 635), ((600,635))], fill=rectangle_color3)

    if len(projectAmenities) == 4:
        draw.rectangle([(20, 20), ((600,635))], fill=rectangle_color2) # Large Rectangle

        draw.rectangle([(20, 190), ((600,190))], fill=rectangle_color3)
        draw.rectangle([(20, 330), ((600,330))], fill=rectangle_color3)
        draw.rectangle([(20, 480), ((600,480))], fill=rectangle_color3)
      
    if len(projectAmenities) == 3:
        draw.rectangle([(20, 20), ((600,480))], fill=rectangle_color2) # Large Rectangle

        draw.rectangle([(20, 190), ((600,190))], fill=rectangle_color3)
        draw.rectangle([(20, 330), ((600,330))], fill=rectangle_color3)
        draw.rectangle([(20, 480), ((600,480))], fill=rectangle_color3)
        
    if len(projectAmenities) == 2:
        
        draw.rectangle([(20, 20), ((600,330))], fill=rectangle_color2)

        draw.rectangle([(20, 190), ((600,190))], fill=rectangle_color3)
        draw.rectangle([(20, 330), ((600,330))], fill=rectangle_color3)
      
    draw.text((50,30), ("Amenities"),fill=gold_color, font=font2)

    # if len(projectAmenities) == 5:

    if len(projectAmenities) == 5:
        amenities1 = projectAmenities[0]
        amenities2 = projectAmenities[1]
        amenities3 = projectAmenities[2]
        amenities4 = projectAmenities[3]
        amenities5 = projectAmenities[4]
 
        label1 = amenities1["label"]
        label2 = amenities2["label"]
        label3 = amenities3["label"]
        label4 = amenities4["label"]
        label5 = amenities5["label"]

        value1 = amenities1["value"]
        value2 = amenities2["value"]
        value3 = amenities3["value"]
        value4 = amenities4["value"]
        value5 = amenities5["value"]


    if len(projectAmenities) == 4:

        amenities1 = projectAmenities[0]
        amenities2 = projectAmenities[1]
        amenities3 = projectAmenities[2]
        amenities4 = projectAmenities[3]
        
        label1 = amenities1["label"]
        label2 = amenities2["label"]
        label3 = amenities3["label"]
        label4 = amenities4["label"]


        value1 = amenities1["value"]
        value2 = amenities2["value"]
        value3 = amenities3["value"]
        value4 = amenities4["value"]



    if len(projectAmenities) == 3:

        amenities1 = projectAmenities[0]
        amenities2 = projectAmenities[1]
        amenities3 = projectAmenities[2]
        
        label1 = amenities1["label"]
        label2 = amenities2["label"]
        label3 = amenities3["label"]

        value1 = amenities1["value"]
        value2 = amenities2["value"]
        value3 = amenities3["value"]



    if len(projectAmenities) == 2:

        amenities1 = projectAmenities[0]
        amenities2 = projectAmenities[1]
        
        label1 = amenities1["label"]
        label2 = amenities2["label"]

        value1 = amenities1["value"]
        value2 = amenities2["value"]


    if len(projectAmenities) == 1:

        amenities1 = projectAmenities[0]
        
        label1 = amenities1["label"]

        value1 = amenities1["value"]

    # ----------------- Amenities 1 -----------------
    if len(projectAmenities) <= 5 :

        if len(value1) == 4: # Amenities 1

            draw.text((30,80),(label1),fill=text_color1, font=font1)
            draw.text((55, 120),(value1[0]),fill=text_color1, font=font3)
            draw.text((55, 150),(value1[1]),fill=text_color1, font=font3)
            draw.text((355, 120),(value1[2]),fill=text_color1, font=font3)
            draw.text((355, 150),(value1[3]),fill=text_color1, font=font3)

        if len(value1) == 3: # Amenities 1

            draw.text((30,80),(label1),fill=text_color1, font=font1)
            draw.text((55, 120),(value1[0]),fill=text_color1, font=font3)
            draw.text((55, 150),(value1[1]),fill=text_color1, font=font3)
            draw.text((355, 120),(value1[2]),fill=text_color1, font=font3)
        
        if len(value1) == 2: # Amenities 1

            draw.text((30,80),(label1),fill=text_color1, font=font1)
            draw.text((55, 120),(value1[0]),fill=text_color1, font=font3)
            draw.text((55, 150),(value1[1]),fill=text_color1, font=font3)
            
        if len(value1) == 1: # Amenities 1

            draw.text((30,80),(label1),fill=text_color1, font=font1)
            draw.text((55, 120),(value1[0]),fill=text_color1, font=font3)
            

    # ------------ Amenities 2 -------------

    if len(projectAmenities) <= 5 and len(projectAmenities) == 2 or len(projectAmenities) <= 5:

        if len(value2) == 4: # Amenities -2

            draw.text((30,200),(label2),fill=text_color1, font=font1)
            draw.text((55, 240),(value2[0]),fill=text_color1, font=font3)
            draw.text((55, 270),(value2[1]),fill=text_color1, font=font3)
            draw.text((355, 240),(value2[2]),fill=text_color1, font=font3)
            draw.text((355, 270),(value2[3]),fill=text_color1, font=font3)


        if len(value2) == 3: # Amenities -2
        
            draw.text((30,200),(label2),fill=text_color1, font=font1)
            draw.text((55, 240),(value2[0]),fill=text_color1, font=font3)
            draw.text((55, 270),(value2[1]),fill=text_color1, font=font3)
            draw.text((355, 240),(value2[2]),fill=text_color1, font=font3)
        

        if len(value2) == 2: # Amenities -2

            draw.text((30,200),(label2),fill=text_color1, font=font1)
            draw.text((55, 240),(value2[0]),fill=text_color1, font=font3)
            draw.text((55, 270),(value2[1]),fill=text_color1, font=font3)


        if len(value2) == 1: # Amenities -2
        
            draw.text((30,200),(label2),fill=text_color1, font=font1)
            draw.text((55, 240),(value2[0]),fill=text_color1, font=font3)
        

    # ------------ Amenities 3 -------------
    if (len(projectAmenities) <= 5 and len(projectAmenities) == 3) or len(projectAmenities) == 3 or len(projectAmenities) == 5:
        
        if len(value3) == 4: # Amenities -3
        
            draw.text((30,345),(label3),fill=text_color1, font=font1)
            draw.text((55, 395),(value3[0]),fill=text_color1, font=font3)
            draw.text((55, 430),(value3[1]),fill=text_color1, font=font3)
            draw.text((355, 395),(value3[2]),fill=text_color1, font=font3)
            draw.text((355, 430),(value3[3]),fill=text_color1, font=font3)


        if len(value3) == 3: # Amenities -3
        
            draw.text((30,345),(label3),fill=text_color1, font=font1)
            draw.text((55, 395),(value3[0]),fill=text_color1, font=font3)
            draw.text((55, 430),(value3[1]),fill=text_color1, font=font3)
            draw.text((355, 395),(value3[2]),fill=text_color1, font=font3)
        

        if len(value3) == 2: # Amenities -3
        
            draw.text((30,345),(label3),fill=text_color1, font=font1)
            draw.text((55, 395),(value3[0]),fill=text_color1, font=font3)
            draw.text((55, 430),(value3[1]),fill=text_color1, font=font3)
        

        if len(value3) == 1: # Amenities -3
        
            draw.text((30,345),(label3),fill=text_color1, font=font1)
            draw.text((55, 395),(value3[0]),fill=text_color1, font=font3)
            

    # ------------ Amenities 2 -------------
    if len(projectAmenities) <= 5 and len(projectAmenities) == 4 or len(projectAmenities) == 4 or len(projectAmenities) == 5:

        if len(value4) == 4:  # Amenities -4
        
            draw.text((30,500),(label4),fill=text_color1, font=font1)
            draw.text((55, 550),(value4[0]),fill=text_color1, font=font3)
            draw.text((55, 580),(value4[1]),fill=text_color1, font=font3)
            draw.text((355, 550),(value4[2]),fill=text_color1, font=font3)
            draw.text((355, 580),(value4[3]),fill=text_color1, font=font3)


        if len(value4) == 3:  # Amenities -4
            
            draw.text((30,500),(label4),fill=text_color1, font=font1)
            draw.text((55, 550),(value4[0]),fill=text_color1, font=font3)
            draw.text((55, 580),(value4[1]),fill=text_color1, font=font3)
            draw.text((355, 550),(value4[2]),fill=text_color1, font=font3)


        if len(value4) == 2:  # Amenities -4
        
            draw.text((30,500),(label4),fill=text_color1, font=font1)
            draw.text((55, 550),(value4[0]),fill=text_color1, font=font3)
            draw.text((55, 580),(value4[1]),fill=text_color1, font=font3)



        if len(value4) == 1:  # Amenities -4
            
            draw.text((30,500),(label4),fill=text_color1, font=font1)
            draw.text((55, 550),(value4[0]),fill=text_color1, font=font3)

    
    # ------------ Amenities 1 -------------
    if len(projectAmenities) == 5:
   

        if len(value5) == 4: # Amenities -4
        
            draw.text((30,650),(label5),fill=text_color1, font=font1)
            draw.text((55, 695),(value5[0]),fill=text_color1, font=font3)
            draw.text((55, 730),(value5[1]),fill=text_color1, font=font3)
            draw.text((355, 695),(value5[2]),fill=text_color1, font=font3)
            draw.text((355, 730),(value5[3]),fill=text_color1, font=font3)

        if len(value5) == 3: # Amenities -5
        
            draw.text((30,650),(label5),fill=text_color1, font=font1)
            draw.text((55, 695),(value5[0]),fill=text_color1, font=font3)
            draw.text((55, 730),(value5[1]),fill=text_color1, font=font3)
            draw.text((355, 695),(value5[2]),fill=text_color1, font=font3)

        if len(value5) == 2: # Amenities -5
        
            draw.text((30,650),(label5),fill=text_color1, font=font1)
            draw.text((55, 695),(value5[0]),fill=text_color1, font=font3)
            draw.text((55, 730),(value5[1]),fill=text_color1, font=font3)


        if len(value5) == 1: # Amenities -5
        
            draw.text((30,650),(label5),fill=text_color1, font=font1)
            draw.text((55, 695),(value5[0]),fill=text_color1, font=font3)


    text_color = (255, 255, 255) # white text color
    font = ImageFont.truetype ("arialbd.ttf", 20) # define font and font size

    output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
    # logo = Image.open("sq_logo.png").resize((150,90)).convert("RGBA")
    # output_image.paste(logo, (1050, 2), mask=logo)


    output_image.save("image4.png")
    result = "image4.png"
    # output_image.show()
    return result


# # Sample data you provided
# projectAmenities = [
    # {
    #     "label": "Sports",
    #     "value": ["Gymnasium","Kids' Pool", "Badminton Court(s)", "Tennis Court(s)"]
    # },
    # {
    #     "label": "Convenience",
    #     "value": ["Power Backup", "Lift"]
    # },
    # {
    #     "label": "Safety",
    #     "value": ["Gate Gaurd", "CCTV", "Fire fighting system"]
    # },
    # {
    #     "label": "Leisure",
    #     "value": ["Party hall", "Clubhouse", "Amphitheater", "Indoor Games"]
    # },
    # {
    #     "label": "Enviornment",
    #     "value": ["Rain Water Harvesting", "Large Green Area", "Sewage Treatment Plant"]
    # }
# ]

# fourth_image("1.png", projectAmenities)

