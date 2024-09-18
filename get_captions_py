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

L.login('ian.carscadden', '')  # Your login
PROFILE = "garyvee"
profile = instaloader.Profile.from_username(L.context, PROFILE)

all_captions = []
post_count = 0

print("Fetching posts...")
for post in profile.get_posts():
    if post_count >= 1500:
        break  # Stop after processing 1500 posts

    if post.caption:
        all_captions.append(post.caption)  # Store the raw caption with emojis
    else:
        all_captions.append(None)

    post_count += 1

print("Finished fetching captions.")

# Save as a JSON file
with open("garyvee_captions_final.json", "w", encoding="utf-8") as f:
    json.dump(all_captions, f, ensure_ascii=False, indent=4)  # ensure_ascii=False is key
