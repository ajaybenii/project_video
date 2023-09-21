from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO


def first_listing_image(first_cover_image,listing_type,agent_name,agent_img,agent_designation,contact_no,email_address,agency_logo,property_type,price,yearly_monthly,property_location):
    
    # Create new image with same dimensions as input image
    # new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))
    # first_cover_image = Image.open(first_cover_image).resize((1200,800))
    new_image = Image.new("RGBA", first_cover_image.size, (0, 0, 0, 0))

    # Define color and opacity of rectangle to paste onto new image
    rectangle_color = (0, 0, 0,170) # red with 50% opacity
    rectangle_color1 = (0, 0, 0, 220)
    rectangle_color2 = (255, 165, 0, 150)
    # Paste colored rectangle onto new image
    draw = ImageDraw.Draw(new_image)
    draw.rectangle([(0, 0), ((530,800))], fill=rectangle_color)
    draw.rectangle([(0, 620), ((1200,800))], fill=rectangle_color1)
    draw.rectangle([(840, 520), ((1200,620))], fill=rectangle_color2)

    schedule = "Call me to schedule\n      a showing today"
    text_color = (255, 255, 255) # white text color
    text_color1 = (255, 165, 0)
    font = ImageFont.truetype("arialbd.ttf", 50)
    fontt = ImageFont.truetype("arialbd.ttf", 65)
    font1 = ImageFont.truetype("arialbd.ttf", 45)# define font and font size
    font3 = ImageFont.truetype("arialbd.ttf", 25)


    # Paste text onto new image
    draw.text((950, 540),schedule, fill=text_color, font=font3)
    draw.text((50, 50),listing_type, fill=text_color, font=fontt)
    draw.text((50, 140),property_type, fill=text_color1, font=font1)
    draw.text((50, 360),("Rs "+price), fill=text_color, font=font)
        
    font = ImageFont.truetype("arialbd.ttf", 20) # define font and font size
    font2 = ImageFont.truetype("arialbd.ttf", 20)
    font4 = ImageFont.truetype("arialbd.ttf", 24)
    
    draw.text((50, 433),property_location, fill=text_color, font=font4)
    
  
    if agency_logo == "string" or " " or "":

        pass
    
    else:
        try:
            output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
            response_logo = requests.get(agency_logo)
            agency_logo = Image.open(BytesIO(response_logo.content)).convert("RGBA").resize((120,120))
            output_image.paste(agency_logo, (1000, 650), mask=agency_logo)
        except:
            return({"response":"Agency logo image url is not  valid"})
        
    # agent_img = Image.open(agent_img).convert("RGBA").resize((200,200))

    if agent_img == "":

        draw.text((40, 630),agent_name, fill=text_color, font=font)
        draw.text((40, 660),agent_designation, fill=text_color, font=font2)
        draw.text((80, 720),contact_no, fill=text_color, font=font)
        draw.text((80, 750),email_address, fill=text_color, font=font2)
        
        output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)

        mobile_logo = Image.open("mobile_logo.png").resize((20,20)).convert("RGBA")
        output_image.paste(mobile_logo, (40, 720), mask=mobile_logo)

        email_logo = Image.open("email_logo.png").resize((20,20)).convert("RGBA")
        output_image.paste(email_logo, (40, 750), mask=email_logo)
        
        # response_agent = requests.get(agent_img)
        # agent_img = Image.open("agent_default_image.jpg").convert("RGBA").resize(((200,200)))
        # output_image
    
    else:
        try:

            draw.text((280, 630),agent_name, fill=text_color, font=font)
            draw.text((280, 660),agent_designation, fill=text_color, font=font2)

            draw.text((310, 720),contact_no, fill=text_color, font=font)
            draw.text((310, 750),email_address, fill=text_color, font=font2)

            output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
            
            mobile_logo = Image.open("mobile_logo.png").resize((20,20)).convert("RGBA")
            output_image.paste(mobile_logo, (280, 720), mask=mobile_logo)

            email_logo = Image.open("email_logo.png").resize((20,20)).convert("RGBA")
            output_image.paste(email_logo, (280, 750), mask=email_logo)
            
            response_agent = requests.get(agent_img)
            agent_img = Image.open(BytesIO(response_agent.content)).convert("RGBA").resize(((200,200)))
            output_image.paste(agent_img, (50, 600), mask=agent_img)

        except:
            return{"Agent image url not valid"}
        
    # output_image = Image.alpha_composite(first_cover_image.convert("RGBA"), new_image)
    # location_img = Image.open("location.png").resize((20,20)).convert("RGBA")
    # output_image.paste(location_img, (50, 435), mask=location_img)

    logo = Image.open("sy_logo_black.jpg").resize((150,70)).convert("RGBA")
    output_image.paste(logo, (1050, 2), mask=logo)

    # logo = Image.open("location.png").resize((20,20)).convert("L")
    # output_image.paste(logo, (400, 605), mask=logo)

    # Save output image
    # output_image.show()
    output_image.save("output_image.png")
    # output_image.show()
    result = "output_image.png"
    return result

# first_image('first_cover_image', 'listing_type', 'agency_logo', 'property_type', 'price', 'yearly_monthly', 'property_location')
# first_listing_image(first_cover_image = "1.png",
# listing_type = "For rent",
# agent_img = "",
# agent_name= "Mr. Vivek Agarwal",
# agent_designation= "Sales product manager",
# contact_no = "+91 9028302838",
# email_address = "vivek.squareyard@com.in",
# agency_logo = "alogo.png",
# property_type = "Townhouse",
# price = "1,20,00,000",
# yearly_monthly = "yearly",
# property_location = "south city, Dubai")
