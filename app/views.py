from django.shortcuts import render
import requests
import urllib.parse
from django.http import HttpResponse
import instaloader
import os
import requests
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import requests
from urllib.parse import quote_plus

# Get instance
L = instaloader.Instaloader()

# Create your views here.

def home(request):
    context =  {}
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            # username = input_text.split("/")[-2]
            context = crawlbase_api(input_text)
    else:
        form = MyForm()
    context['form'] = form

    return render(request, 'app/index.html', context)


def crawlbase_api(url):
    whole_context = {}
    context = {}
    # url = quote_plus(url)
    # api_url = f'https://api.crawlbase.com/?token=W264dTzZkuGre1nd2a6YLA&url={url}&scraper=instagram-profile'

    # response = requests.get(api_url)

    # print(response.status_code)  # HTTP status code
    # json_resp = response.json()
    # print(json_resp)  # Response content as text

    # posts = json_resp['body']['posts']
    # cnt = 0
    # for post in posts:
 
    #     print(post['image'])
    #     context[post['image']] = 'image'
    #     cnt+=1
    #     if cnt==5:
    #          break
    context['https://instagram.fccu1-2.fna.fbcdn.net/v/t51.2885-15/357768070_648586263855491_7640280198118386154_n.jpg?stp=dst-jpg_e35_p1080x1080&_nc_ht=instagram.fccu1-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=p6kJS1a2mzIAX_HGey2&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfBYOkaPiR0l2XPu3DJZaEooCsDGYUHt4rNmJk8ENZaxoQ&oe=64AB0D8C&_nc_sid=8b3546'] = 'image'
    # instascrapeway()
    whole_context['context'] = context

    return whole_context


def instascrapeway(username):

    L = instaloader.Instaloader()

    L.login("fortcony", "Gasttozz123@") 
    whole_context = {}
    context = {}
    profile = instaloader.Profile.from_username(L.context, username)
    profile_image_url = profile.get_profile_pic_url()
    response = requests.get(profile_image_url)
    filename = "profile_image.jpg"  # Replace with the desired filename and extension
    with open(filename, "wb") as f:
            f.write(response.content)
    whole_context['profile_pic'] = uploadMedia(filename)
    whole_context['username'] = profile.username
    cnt = 0
    for post in profile.get_posts():
        #cover profiles with less than 5 posts too       
        if post.mediacount > 1:
            multiple = post.get_sidecar_nodes()
            for media in multiple:
                if media.is_video:
                    response = requests.get(media.video_url)
                    filename = "video" + str(cnt) + ".mp4"  # Replace with the desired filename and extension
                    filename2 = "2video" + str(cnt) + ".mp4"  # Replace with the desired filename and extension
                    with open(filename, "wb") as f:
                        f.write(response.content)
                    ffmpeg_extract_subclip(filename, 0, 5, targetname=filename2)
                    context[uploadMedia(filename2)] = 'video'
                else:
                    response = requests.get(media.display_url)
                    filename = "image" + str(cnt) + ".jpg"  # Replace with the desired filename and extension
                    with open(filename, "wb") as f:
                            f.write(response.content)
                    context[uploadMedia(filename)] = 'image'
                break
        else:
            if post.is_video:
                response = requests.get(post.video_url)
                filename = "video" + str(cnt) + ".mp4"  # Replace with the desired filename and extension
                filename2 = "2video" + str(cnt) + ".mp4"  # Replace with the desired filename and extension
                with open(filename, "wb") as f:
                        f.write(response.content)
                ffmpeg_extract_subclip(filename, 0, 5, targetname=filename2)
                context[uploadMedia(filename2)] = 'video'
            else:
                response = requests.get(post.url)
                filename = "image" + str(cnt) + ".jpg"  # Replace with the desired filename and extension
                with open(filename, "wb") as f:
                            f.write(response.content)
                context[uploadMedia(filename)] = 'image'
        cnt+=1
        if (cnt==5):
            break
    whole_context['context'] = context

    delete_files_with_extensions(file_extensions)

    return whole_context
import os

def delete_files_with_extensions(extensions):
    for filename in os.listdir():
        if any(filename.endswith(ext) for ext in extensions):
            file_path = os.path.join(filename)
            os.remove(file_path)
            print(f"Deleted file: {filename}")

# Directory path where the files are located
directory_path = "/path/to/directory"

# Extensions of files to delete (in this case, .mp3 and .jpg)
file_extensions = [".mp4", ".jpg"]

# Call the function to delete files




def uploadMedia2(filename):
     return "https://ik.imagekit.io/ze7cq8teis/test_upload_CCc8oDyf1"

def uploadMedia(filename):
    # current_directory = os.path.dirname(os.path.abspath(__file__)) + "/images.jpeg"
    current_directory = filename
    with open(current_directory, "rb") as img_file:
        from imagekitio import ImageKit

        imagekit = ImageKit(
            public_key='public_YpxbB0jz1ysOBAm8ELUAQ2Da2gA=',
            private_key='private_wc+FHkegHJK6O1+xFQ5tL79qZ/Y=',
            url_endpoint = 'https://ik.imagekit.io/ze7cq8teis/'
        )

        upload = imagekit.upload(
            file=img_file,
            file_name="test_upload",
        )

        # Raw Response
        return(upload.response_metadata.raw['url'])


from .forms import MyForm

def home2(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            # Call your function with input_text as the parameter
            print(input_text)
    else:
        form = MyForm()

    return render(request, 'app/index.html', {'form': form})


