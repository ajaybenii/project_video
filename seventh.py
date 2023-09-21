from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


def seventh_image(first_cover_image,landmarks):
    
    first_cover_image = Image.open(first_cover_image).resize((1200,800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
    
    # Define color and opacity of rectangle to paste onto new image

    rectangle_color1 = (60,179,113)
    rectangle_color2 = (0, 0, 0, 180)
    rectangle_color3 = (255,255,255,50)

    draw = ImageDraw.Draw(new_image)

    font = ImageFont.truetype("arialbd.ttf", 23)
    font1 = ImageFont.truetype("arialbd.ttf", 20)
    font2 = ImageFont.truetype("arialbd.ttf", 15)
    font3 = ImageFont.truetype("arialbd.ttf", 12)

    gold_color = (255,215,0)
    text_color1 = (255, 255, 255)
    text_color2 = (0,191,255)
    
    item_0 = landmarks[0]
    item_1 = landmarks[1]
    item_2 = landmarks[2]

    label_0 = item_0["label"]
    label_1 = item_1["label"]
    label_2 = item_2["label"]

    value_0 = item_0["value"]
    value_1 = item_1["value"]
    value_2 = item_2["value"]

    
    if len(landmarks) == 3:
        # print("if =6")

        draw.rectangle([(5, 5), ((250,350))], fill=rectangle_color1) # Green Rectangle
        draw.rectangle([(10, 10), ((600,780))], fill=rectangle_color2) # Large Rectangle

        draw.rectangle([(10, 125), ((600,125))], fill=rectangle_color3)
        draw.rectangle([(10, 200), ((600,200))], fill=rectangle_color3)
        draw.rectangle([(10, 380), ((600,380))], fill=rectangle_color3)
        draw.rectangle([(10, 460), ((600,460))], fill=rectangle_color3)
        draw.rectangle([(10, 620), ((600,620))], fill=rectangle_color3)
        draw.rectangle([(10, 700), ((600,700))], fill=rectangle_color3)

        draw.text((20,15), ("Nearby Landmarks"),fill=gold_color, font=font)

        draw.text((20,50),(label_0),fill=text_color2, font=font1)
        draw.text((20, 280),(label_1),fill=text_color2, font=font1)
        draw.text((20, 530),(label_2),fill=text_color2, font=font1)

    if len(landmarks) == 2:
        # print("if =6")

        draw.rectangle([(5, 5), ((250,350))], fill=rectangle_color1) # Green Rectangle
        draw.rectangle([(10, 10), ((600,550))], fill=rectangle_color2) # Large Rectangle

        draw.rectangle([(10, 120), ((600,120))], fill=rectangle_color3)
        draw.rectangle([(10, 200), ((600,200))], fill=rectangle_color3)
        draw.rectangle([(10, 380), ((600,380))], fill=rectangle_color3)
        draw.rectangle([(10, 460), ((600,460))], fill=rectangle_color3)


        draw.text((20,15), ("Nearby Landmarks"),fill=gold_color, font=font)

        draw.text((20,50),(label_0),fill=text_color1, font=font1)
        draw.text((20, 280),(label_1),fill=text_color1, font=font1)
 

    if len(landmarks) == 1:
        # print("if =6")

        draw.rectangle([(5, 5), ((200,200))], fill=rectangle_color1) # Green Rectangle
        draw.rectangle([(10, 10), ((600,280))], fill=rectangle_color2) # Large Rectangle

        draw.rectangle([(10, 120), ((600,120))], fill=rectangle_color3)
        draw.rectangle([(10, 200), ((600,200))], fill=rectangle_color3)

        draw.text((20,15), ("Nearby Landmarks"),fill=gold_color, font=font)

        draw.text((20,50),(label_0),fill=text_color1, font=font1)


    if len(value_0) == 3:
        
        
        draw.text((20, 80),(value_0[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 100),(value_0[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 90),(value_0[0]["distance"]),fill=text_color1, font=font2)

        draw.text((20, 140),(value_0[1]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 165),(value_0[1]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 155),(value_0[1]["distance"]),fill=text_color1, font=font2)
        
        draw.text((20, 225),(value_0[2]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 250),(value_0[2]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 240),(value_0[2]["distance"]),fill=text_color1, font=font2)


    if len(value_0) == 2:
        
        
        draw.text((20, 80),(value_0[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 100),(value_0[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 90),(value_0[0]["distance"]),fill=text_color1, font=font2)

        draw.text((20, 140),(value_0[1]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 165),(value_0[1]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 155),(value_0[1]["distance"]),fill=text_color1, font=font2)


    if len(value_0) == 1:
        
        draw.text((20, 80),(value_0[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 100),(value_0[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 90),(value_0[0]["distance"]),fill=text_color1, font=font2)


    if len(value_1) == 3:
         
        draw.text((20, 325),(value_1[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 350),(value_1[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 335),(value_1[0]["distance"]),fill=text_color1, font=font2)

        draw.text((20, 400),(value_1[1]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 425),(value_1[1]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 410),(value_1[1]["distance"]),fill=text_color1, font=font2)
        
        draw.text((20, 480),(value_1[2]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 505),(value_1[2]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 490),(value_1[2]["distance"]),fill=text_color1, font=font2)


    if len(value_1) == 2:
        
        draw.text((20, 325),(value_1[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 350),(value_1[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 335),(value_1[0]["distance"]),fill=text_color1, font=font2)

        draw.text((20, 400),(value_1[1]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 425),(value_1[1]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 410),(value_1[1]["distance"]),fill=text_color1, font=font2)
        

    if len(value_1) == 1:
        
        draw.text((20, 325),(value_1[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 350),(value_1[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 335),(value_1[0]["distance"]),fill=text_color1, font=font2)



    if len(value_2) == 3:
        
        draw.text((20, 565),(value_2[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 590),(value_2[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 570),(value_2[0]["distance"]),fill=text_color1, font=font2)

        draw.text((20, 640),(value_2[1]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 665),(value_2[1]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 655),(value_2[1]["distance"]),fill=text_color1, font=font2)
        
        draw.text((20, 720),(value_2[2]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 745),(value_2[2]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 735),(value_2[2]["distance"]),fill=text_color1, font=font2)

    if len(value_2) == 2:
        
        draw.text((20, 565),(value_2[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 590),(value_2[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 570),(value_2[0]["distance"]),fill=text_color1, font=font2)

        draw.text((20, 640),(value_2[1]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 665),(value_2[1]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 655),(value_2[1]["distance"]),fill=text_color1, font=font2)
        

    if len(value_2) == 1:
        
        draw.text((20, 565),(value_2[0]["landmarkName"]),fill=text_color1, font=font2)
        draw.text((20, 590),(value_2[0]["localityName"]),fill=text_color1, font=font3)
        draw.text((440, 570),(value_2[0]["distance"]),fill=text_color1, font=font2)


    text_color = (255, 255, 255) # white text color
    font = ImageFont.truetype ("arialbd.ttf", 20) # define font and font size

    try:
        output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
        output_image.save("image7.png")
        result = "image7.png"
        return result
    except Exception as e:
        return f"Error saving image: {str(e)}"

# first_image(first_cover_image = "1.jpg",
#         nearby_landmarks= ("Schools",),
#         landmarks_data1 = ("Schools","Bal Bharati Public School","Sector 59","3.02 KM",),
#         landmarks_data2 = (""),
#         landmarks_data3 = ("") )



# landmarks = [
    # {
    #     "label": "School",
    #     "value": [
    #         {
    #             "landmarkName": "Pragyanam School",
    #             "localityName": "Sector 63",
    #             "distance": "0.24 km"
    #         },
    #         {
    #             "landmarkName": "Tagore Public School",
    #             "localityName": "Sector 50",
    #             "distance": "1.28 km"
    #         },
    #         {
    #             "landmarkName": "Bal Bharati Public School",
    #             "localityName": "Sector 40",
    #             "distance": "2.28 km"
    #         }
    #     ]
    # },
    # {
    #     "label": "Hospital",
    #     "value": [
    #         {
    #             "landmarkName": "Prakash Hospital",
    #             "localityName": "Sector 60",
    #             "distance": "1.24 km"
    #         },
    #         {
    #             "landmarkName": "Life Care Hospital Manesar",
    #             "localityName": "Sector 55",
    #             "distance": "1.08 km"
    #         },
    #         {
    #             "landmarkName": "Fortis hospital",
    #             "localityName": "Sector 45",
    #             "distance": "2.18 km"
    #         }
    #     ]
    # },
    # {
    #     "label": "Shopping Center",
    #     "value": [
    #         {
    #             "landmarkName": "Safe Mart",
    #             "localityName": "Sector 56",
    #             "distance": "1.24 km"
    #         },
    #         {
    #             "landmarkName": "Sodhi market",
    #             "localityName": "Sector 55",
    #             "distance": "1.08 km"
    #         },
    #         {
    #             "landmarkName": "Apollo care",
    #             "localityName": "Sector 45",
    #             "distance": "2.18 km"
    #         }
    #     ]
    # }
# ]

# seventh_image(first_cover_image="1.png", landmarks=landmarks)
