import instaloader
import json

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False
)
# Login to instagram using your username and password
# Pass in your information below as ("username", "password")

L.login('Your username', 'Your password')  # Your login

# Enter the username of the account you want to pull captions form below 
PROFILE = "Username"
profile = instaloader.Profile.from_username(L.context, PROFILE)

all_captions = []
post_count = 0

""" SPECIFY THE AMOUNT OF POSTS YOU WANT TO PULL CAPTIONS FROM BELOW """
specefied_amount = 10

print("Fetching posts...")
for post in profile.get_posts():
    if post_count >= specified_amount:
        break  # Stop after processing 1500 posts

    if post.caption:
        all_captions.append(post.caption)  # Store the raw caption with emojis
    else:
        all_captions.append(None)

    post_count += 1

print("Finished fetching captions.")

# Save as a JSON file, set to save as raw_captions.json
with open("raw_captions.json", "w", encoding="utf-8") as f:
    json.dump(all_captions, f, ensure_ascii=False, indent=4)  # ensure_ascii=False is key
