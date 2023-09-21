# from PIL import Image, ImageDraw, ImageFont

# def fifth_image(first_cover_image, specifications):
#     first_cover_image = Image.open(first_cover_image).resize((1200, 800))
#     new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))

#     # Define colors and opacity of rectangles
#     rectangle_color1 = (60, 179, 113)
#     rectangle_color2 = (0, 0, 0, 180)
#     rectangle_color3 = (255, 255, 255, 50)

#     draw = ImageDraw.Draw(new_image)

#     gold_color = (255, 215, 0)
#     text_color1 = (255, 255, 255)
#     font = ImageFont.truetype("arialbd.ttf", 23)
#     font2 = ImageFont.truetype("arial.ttf", 17)
#     font3 = ImageFont.truetype("arialbd.ttf", 18)

#     # Rectangle dimensions
#     rect_width = 600
#     rect_height = 50
#     spacing = 70

#     y_start = 200


#     draw.rectangle([(100, y_start), ((100 + rect_width + 50, y_start + (spacing * len(specifications))))] , fill=rectangle_color2)
#     draw.rectangle([(100, 150), ((100 + rect_width + 50, y_start + (spacing * len(specifications))))] , fill=rectangle_color2)
#     draw.text((120, 165), "Specifications", fill=gold_color, font=font)

#     for idx, spec in enumerate(specifications):
#         label = spec["label"]
#         value = spec["value"]
        
#         draw.rectangle([(130, y_start + (spacing * idx)), (140 + rect_width, y_start + rect_height + (spacing * idx))], fill=rectangle_color2)
#         draw.text((140, y_start + 20 + (spacing * idx)), label, fill=text_color1, font=font3)
#         draw.text((440, y_start + 20 + (spacing * idx)), value, fill=text_color1, font=font2)

#     output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
#     output_image.save("image5.png")
#     # output_image.show()
#     result = "image5.png"
#     return result

# # Data to replace in the code
# specifications = [
#     {
#         "label": "Master Bedroom-Walls",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Master Bedroom-Flooring",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Other Bedrooms-Flooring",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Walls",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Living Area-Flooring",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Structure",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     }
# ]

# fifth_image(first_cover_image="1.png", specifications=specifications)

from PIL import Image, ImageDraw, ImageFont

def fifth_image(first_cover_image, specifications):
    first_cover_image = Image.open(first_cover_image).resize((1200, 800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))

    # Define colors and opacity of rectangles
    rectangle_color1 = (60, 179, 113)
    rectangle_color2 = (0, 0, 0, 180)
    rectangle_color3 = (255, 255, 255, 50)

    draw = ImageDraw.Draw(new_image)

    gold_color = (255, 215, 0)
    text_color1 = (255, 255, 255)
    font = ImageFont.truetype("arialbd.ttf", 23)
    font2 = ImageFont.truetype("arial.ttf", 18)
    font3 = ImageFont.truetype("arialbd.ttf", 18)

    # Rectangle dimensions
    rect_width = 670
    rect_height = 50
    spacing = 90

    y_start = 200

    draw.rectangle([(100, y_start), ((100 + rect_width + 50, y_start + (spacing * len(specifications))))] , fill=rectangle_color2)
    draw.rectangle([(100, 150), ((100 + rect_width + 50, y_start + (spacing * len(specifications))))] , fill=rectangle_color2)
    draw.text((120, 165), "Specifications", fill=gold_color, font=font)

    for idx, spec in enumerate(specifications):
        label = spec["label"]
        values = spec["value"]
        
        draw.rectangle([(130, y_start + (spacing * idx)), (140 + rect_width, y_start + rect_height + (spacing * idx))], fill=rectangle_color2)
        draw.text((140, y_start + 40 + (90 * idx)), label, fill=text_color1, font=font3)
        
        for val_idx, value in enumerate(values):
            draw.text((440, y_start + 20 + 20 * val_idx + (spacing * idx)), value, fill=text_color1, font=font2)

    output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
    output_image.save("image5.png")
    # output_image.show()
    result = "image5.png"
    return result


# "specifications": [
#     {
#         "label": "Master Bedroom-Walls",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Master Bedroom-Flooring",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Other Bedrooms-Flooring",
#         "value": ["Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Walls",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Living Area-Flooring",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     },
#     {
#         "label": "Structure",
#         "value": ["RCC Frame Structure with infill brick walls","Italian/Imported Marble","Fully Equipped Modular Kitchen"]
#     }
# ]

# fifth_image(first_cover_image="1.png", specifications=specifications)
