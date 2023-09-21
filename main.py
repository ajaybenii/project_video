import os
import requests

import numpy as np
import moviepy.editor as mp

from typing import List
from PIL import Image
from fastapi import FastAPI,HTTPException

# from englisttohindi.englisttohindi import EngtoHindi

from PIL import Image
from io import BytesIO
from typing import Optional
from urllib.parse import urlparse
from pydantic import BaseModel

from fastapi import FastAPI, Response
from fastapi.param_functions import Query
from fastapi.middleware.cors import CORSMiddleware
from moviepy.editor import AudioFileClip
from dotenv import load_dotenv

from first import first_image
from second import second_image
from third import third_image
from fourth import fourth_image
from fifth import fifth_image
from sixth import sixth_image
from seventh import seventh_image 
from eighth import eighth_image

app = FastAPI(
    title="Video genration",
    description="classify images into different categories")


origins = [
    "https://app.smartagent.ae",
    "https://localhost:8081",
    "https://uatapp.smartagent.ae",
    "http://app.smartagent.ae",
    "http://localhost:8081",
    "http://uatapp.smartagent.ae",
    "https://app.smartagent.ae/*",
    "https://localhost:8081/*",
    "https://uatapp.smartagent.ae/*",
    "http://app.smartagent.ae/*",
    "http://localhost:8081/*",
    "http://uatapp.smartagent.ae/*"
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Constants
AUDIO_FILE_NAME = "audio.aac"
AMBIENT_SOUND_FILE_NAME = "ambient.aac"
MERGED_AUDIO_FILE_NAME = "merged.aac"
AMBIENT_FADEOUT_DURATION = 1 # seconds
INTRO_CLIP_DURATION = 5 # seconds
OUTPUT_SIZE = (1200, 800)
CODEC = "libx264"
FPS = 24
VOICEOVER_LANGUAGE='en'


default_img_path = "agent_default_image.jpg"


@app.get("/")
async def root():
    return "Api is working"


class Item(BaseModel):

    image_url: Optional[List[str]]
    project_name : str
    location : str
    price : str
    units : str
    Configuration : (str)
    priceList : List
    projectAmenities : List
    specifications : List
    connection_roads : List
    landmarks : List
    developer_data : dict



@app.post("/generate_project_video")
# async def get_video(cover_image:Optional[str],agent_logo: Optional[str],agent_name:Optional[str],consultancy_name:Optional[str],contact_no:Optional[str],property_type:Optional[str],project:str,price_property:Optional[str],yearly_monthly:Optional[str],email_address:Optional[str],locality:Optional[str],bedroom:Optional[str],bathroom:Optional[str],area:Optional[str],agent_img: str=None):
async def get_video(item:Item,audio_type: str = Query("music", enum=["music"])):
        
        img_list=[]
        n = 0
        x=1

        try :
            for i in range (len(item.image_url)):
                
                    response = requests.get(item.image_url[n])        
                    cover_image = Image.open(BytesIO(response.content)).convert("RGBA").resize((1200,800))
                    cover_image.save(f"{x}.png")
                    print("get image = ",x)
                    img_list.append(str(f"{x}.png"))
                    
                    # print("length of img_list = ",len(img_list))
                    n+=1
                    x+=1
                    
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Image error {item.image_url[n]}")

        image_duration = 3

        # Load the audio file
        audio_file = 'music.acc'
        audio = AudioFileClip(audio_file)

        # Create a list of clips from the image files
        size = (1200, 800)
        final_clips = []
        
        if len(img_list) == 8:
            slide = [(first_image(str(img_list[0]),item.project_name,item.location,item.price)),
                    (second_image(str(img_list[1]),item.units,item.Configuration)),
                    (third_image(str(img_list[2]),item.priceList)),
                    (fourth_image(str(img_list[3]),item.projectAmenities)),
                    (fifth_image(str(img_list[4]),item.specifications)),
                    (sixth_image(str(img_list[5]),item.connection_roads)),
                    (seventh_image(str(img_list[6]),item.landmarks)),
                    (eighth_image(str(img_list[7]),item.developer_data))
                    ]
        x=0
        num = 1
        for img in img_list:

            image_clip = mp.ImageClip(img, duration=4)

            slide = image_clip.resize(lambda t: 1 + 0.04 * t)  # Zoom-in effect
            with_text = mp.ImageClip(f"image{num}.png")
            # slide = slide.crop(x_center=0.5, y_center=0.5, width=1.2, height=1.2)  # Adjust the zoom level as per your preference
            slide = slide.set_position(('center', 'center'))

            num += 1
   
            # Paste logo on every image
            logo_img = Image.open("sy_logo_black.jpg").resize((150,70)).convert("RGBA")
            logo_img.save("logo.png")
            logo = mp.ImageClip("logo.png").set_position((1050,2))
            
            slide = mp.CompositeVideoClip([slide,logo], size=size)
            slide = slide.set_duration(image_duration)


            slide_with_txt = mp.CompositeVideoClip([with_text,logo], size=size)
            slide_with_txt = slide_with_txt.set_duration(2)
            
            final_clips.append(slide_with_txt)
            final_clips.append(slide)

        video = mp.concatenate_videoclips(final_clips)

        # Set the audio for the video
        audio = audio.set_duration(len(img_list)*5)
        video = video.set_audio(audio)

        # Write the final video with audio to a file
        video.write_videofile('output_video.mp4', codec='libx264',fps=24,audio_codec='aac')
                # Open the video file and read its contents
        
        with open("output_video.mp4", mode="rb") as file:
            video = file.read()

        # Create a response with the video data and the "video/mp4" media type
        response = Response(content=video, media_type="video/mp4")

        # Set the Content-Disposition header to "attachment" to force a download dialog
        response.headers["Content-Disposition"] = "attachment"

        # Return the response
        return response