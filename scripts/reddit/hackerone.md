## Summary:
All pictures in private chats are exposed to the public.

## Impact:
The potential impact is that a bad actor can try and find and possibly download all the images that are sent privately and also target specific users / even admins if they have a time frame of when a person sent a picture. 

## Steps To Reproduce:
You can easily reproduce this issue by having two chat accounts message each other pictures.

  1. "Account A" sends a picture to "Account B".
  1. Right click on the image and click on "Copy Image Address". 
  1. Paste it in URL in incognito mode and you should see the picture. If you are not logged into Reddit in incognito mode you will still see the picture.

## Supporting Material/References:
Here's a sample image from my chat you can see: https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F16fz7frfwqoc1.png

Luckily if a user deletes the picture in their chat it can disappear.

  * [attachment / reference]
However if you look closer we can see all images go to the same path in the URL: 
- https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F16fz7frfwqoc1.png
    - They are all saved in this path: https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F
    - Followed by "file_name.file_type"
    - **https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2F**_**16fz7frfwqoc1.png**_
        - You start noticing it's consistently a string of 13 characters.  You also notice the last 4 -- 8 digits don't change much.

{F3124870} 
- Here I consistently sent photos and noticed that the last 4 -- 8 digits stay the same and usually "increment". I added the "|" for emphasis of the "chunks".
    - A picture I sent earlier ended in "joc1". A picture posted earlier in front page of reddit is "noc1".  And now from these photos you can see "joc1".
    - The next batch of 4 from the end are also "incrementing".
        - "fijt" --> " lijt" --> "0jjt" --> "0ckt"
        - The reason there is some skipping is because multiple users are always chatting and uploading pictures in between the timefrome.
    - Based on that the bad actor can guess and only need to do a combination of the first 5 letters/numbers to find a specific photo or a person's photo reducing the complexity immediately and making it easy for them to get photos from a specific timeframe. I believe this URL saves all images including those from public posts, to private chats and also admins.

## Impact

An attacker can target and download all photos saved on the server. They can also download photos from a specific time frame if they wanted. They can find private chat photos even if it's admins chatting with each other, public posts or users chatting with one another.