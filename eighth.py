from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def eighth_image(first_cover_image, developer_data):
    
    first_cover_image = Image.open(first_cover_image).resize((1200,800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
    
    # Define color and opacity of rectangle to paste onto new image
    rectangle_color1 = (60,179,113)
    rectangle_color2 = (0, 0, 0, 200)
    
    # Paste colored rectangle onto new image
    draw = ImageDraw.Draw(new_image)
    
    draw.rectangle([(120, 480), ((300,650))], fill=rectangle_color1)
    draw.rectangle([(140, 500), ((650,700))], fill=rectangle_color2)
    
    text_color = (255, 255, 255) # white text color

    font = ImageFont.truetype("arialbd.ttf", 28)
    font1 = ImageFont.truetype("arialbd.ttf", 22)
    font2 = ImageFont.truetype("arialbd.ttf", 27)
    font3 = ImageFont.truetype("arialbd.ttf", 17)

    text_color1 = (255, 255, 255)
    rs_text_color =(238,130,238) 

    company_logo = (developer_data["image"])
    project_name = developer_data["name"]
    experience = "Experience: " + str(developer_data["experience"]) + " years"
    on_going_projects = "On Going Projects: " + str(developer_data["ongoingprojects"])
    past_projects = "Past Projects: " + str(developer_data["pastprojects"])

    draw.text((155, 505), (f"{project_name}"), fill=text_color1, font=font)
    draw.text((155, 545), (f"{experience}"), fill=text_color, font=font3)
    draw.text((290, 590), (f"{on_going_projects}"), fill=text_color, font=font1)
    draw.text((290, 640), (f"{past_projects}"), fill=text_color, font=font1)
    
    text_color = (255, 255, 255) # white text color
    font = ImageFont.truetype("arialbd.ttf", 20) # define font and font size

    output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)

    response_company_logo = requests.get(company_logo)
    comp_logo = Image.open(BytesIO(response_company_logo.content)).resize((100,100)).convert("RGBA")
    output_image.paste(comp_logo, (160,580), mask=comp_logo)

    output_image.save("image8.png")
    result = "image8.png"
    # output_image.show()
    return result

# developer_data = {
#     "image": "https://static.squareyards.com/resources/images/developerlogo/maxheights-group-139.jpg",
#     "ongoingprojects": 2,
#     "pastprojects": 1,
#     "name": "Maxheights",
#     "experience": 0
# }

# company_logo = developer_data["image"]
# project_name = developer_data["name"]
# experience = "Experience: " + str(developer_data["experience"]) + " years"
# on_going_projects = "On Going Projects: " + str(developer_data["ongoingprojects"])
# past_projects = "Past Projects: " + str(developer_data["pastprojects"])

# eighth_image("1.png",developer_data = {
#     "image": "https://static.squareyards.com/resources/images/developerlogo/maxheights-group-139.jpg",
#     "ongoingprojects": 2,
#     "pastprojects": 1,
#     "name": "Maxheights",
#     "experience": 0
# })
