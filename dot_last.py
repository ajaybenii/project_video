import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


def last_listing_img(last_cover_image,agent_img,agency_logo,agent_name,agent_designation,contact_no,email_address):    

    # Create new image with same dimensions as input image
    
    # last_cover_image = Image.open(last_cover_image).resize((1200,800))
    new_image = Image.new("RGBA", last_cover_image.size, (0, 0, 0, 0))

    # Define color and opacity of rectangle to paste onto new image
    rectangle_color = (0, 0, 0, 200) # red with 50% opacity
    rectangle_color1 = (255, 165, 0, 150)
    # Paste colored rectangle onto new image
    draw = ImageDraw.Draw(new_image)
    draw.rectangle([(0, 620), ((1200,800))], fill=rectangle_color)

    draw.rectangle([(840, 520), ((1200,620))], fill=rectangle_color1)

    schedule = "Call me to schedule\n      a showing today"
    text_color = (255, 255, 255) # white text color

    font = ImageFont.truetype("arialbd.ttf", 20) # define font and font size
    font2 = ImageFont.truetype("arialbd.ttf", 20)
    font1 = ImageFont.truetype("arialbd.ttf", 25)

    # Paste text onto new image
    draw.text((950, 540),schedule, fill=text_color, font=font1)

    if agent_img == "":

        draw.text((40, 630),agent_name, fill=text_color, font=font)
        draw.text((40, 660),agent_designation, fill=text_color, font=font2)
        draw.text((80, 720),contact_no, fill=text_color, font=font)
        draw.text((80, 750),email_address, fill=text_color, font=font2)
        # response_agent = requests.get(agent_img)
        output_image = Image.alpha_composite(last_cover_image.convert("RGBA"), new_image)
        # agent_img = Image.open("agent_default_image.jpg").convert("RGBA").resize(((200,200)))
        # output_image.paste(agent_img, (50, 600), mask=agent_img)

        mobile_logo = Image.open("mobile_logo.png").resize((20,20)).convert("RGBA")
        output_image.paste(mobile_logo, (40, 720), mask=mobile_logo)

        email_logo = Image.open("email_logo.png").resize((20,20)).convert("RGBA")
        output_image.paste(email_logo, (40, 750), mask=email_logo)

    
    else:
        
        try:
            
            draw.text((280, 630),agent_name, fill=text_color, font=font)
            draw.text((280, 660),agent_designation, fill=text_color, font=font2)
            draw.text((310, 720),contact_no, fill=text_color, font=font)
            draw.text((310, 750),email_address, fill=text_color, font=font2)
            
            output_image = Image.alpha_composite(last_cover_image.convert("RGBA"), new_image)

            response_agent = requests.get(agent_img)
            agent_img = Image.open(BytesIO(response_agent.content)).convert("RGBA").resize(((200,200)))
            output_image.paste(agent_img, (50, 600), mask=agent_img)
            
            mobile_logo = Image.open("mobile_logo.png").resize((20,20)).convert("RGBA")
            output_image.paste(mobile_logo, (280, 720), mask=mobile_logo)

            email_logo = Image.open("email_logo.png").resize((20,20)).convert("RGBA")
            output_image.paste(email_logo, (280, 750), mask=email_logo)

        except:
            return{"Agent image url not valid"}
    
    
    
    logo = Image.open("sy_logo_black.jpg").resize((150,70)).convert("RGBA")
    output_image.paste(logo, (1050, 2), mask=logo)

    if agency_logo == "":
        output_image
    
    else:

        response_logo = requests.get(agency_logo)
        agency_logo = Image.open(BytesIO(response_logo.content)).convert("RGBA").resize((120,120))
        output_image.paste(agency_logo, (1000, 650), mask=agency_logo)
    


    # Save output image
    output_image.save("last_img.png")
    # output_image.show()
    result = "last_img.png"

    return result

# last_listing_img(last_cover_image = "1.png",
#          agent_img = "https://img.staticmb.com/mbcontent/images/uploads/2023/3/small-bedroom-decorating-ideas-on-a-budget.jpg",
#          agency_logo = "https://img.staticmb.com/mbcontent/images/uploads/2023/3/small-bedroom-decorating-ideas-on-a-budget.jpg",
#          agent_name = "Mr. Vivek Agarwal",
#          agent_designation = "",
#          contact_no = "+91 9389393933",
#          email_address = "vivek.squareyards@.com.in")