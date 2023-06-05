import nasapy
import os
from datetime import datetime
import urllib.request
from IPython.display import Image, display, Audio
from gtts import gTTS
import tkinter as tk
from PIL import Image as PILImage
from PIL import ImageTk

my_key = '7Xr2lSW5pxc8Ahsg8otgOw9WI7ktEcFw8TsSjcKj'
nasa = nasapy.Nasa(key=my_key)

d = datetime.today().strftime('%Y-%m-%d')

apod = nasa.picture_of_the_day(date=d, hd=True)

if (apod["media_type"] == "image"):
    if ("hdurl" in apod.keys()):

        title = d + "_" + apod["title"].replace(" ", "_").replace(":", "_") + ".jpg"

        img_dir = "./Astro_Images"

        dir_res = os.path.exists(img_dir)

        # Check if the path exists
        if (dir_res == False):
            os.makedirs(img_dir)
        else:
            print("Directory already exists!")

        urllib.request.urlretrieve(url=apod["hdurl"], filename=os.path.join(img_dir, title))

        print("\n")
        choice = input("Press * to hear the audio explanation : ")

        if (choice == "*"):
            mytext = apod["explanation"]

            myobj = gTTS(text=mytext, lang="en", slow=False)

            audio_title = d + "_" + apod["title"] + ".mp3"

            myobj.save(os.path.join(img_dir, audio_title))

            sound_file = os.path.join(img_dir, audio_title)

            display(Audio(sound_file, autoplay=True))

        root = tk.Tk()
        root.title(apod["title"])

        # Open the image file
        img = PILImage.open(os.path.join(img_dir, title))

        resize_image = img.resize((300, 300))

        # Convert the image to a Tkinter-compatible photo image
        tk_img = ImageTk.PhotoImage(img)

        # Create a label and add the image to it
        label = tk.Label(root, image=tk_img)
        label.image = tk_img  # keep a reference to the image
        label.pack()

        root.mainloop()

else:
    print("Sorry, Image not available!")

