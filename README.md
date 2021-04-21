# About Instane
### Selenium Based Instagram Bot
```
 __     __   __     ______     ______   ______     __   __     ______    
/\ \   /\ "-.\ \   /\  ___\   /\__  _\ /\  __ \   /\ "-.\ \   /\  ___\   
\ \ \  \ \ \-.  \  \ \___  \  \/_/\ \/ \ \  __ \  \ \ \-.  \  \ \  __\   
 \ \_\  \ \_\\"\_\  \/\_____\    \ \_\  \ \_\ \_\  \ \_\\"\_\  \ \_____\ 
  \/_/   \/_/ \/_/   \/_____/     \/_/   \/_/\/_/   \/_/ \/_/   \/_____/ 
```                                                                        


#### Instane uses selenium to automate actions based on given cli params in accordance with the necessary configs obtained from "txt" files

# Bot Benchmark

## New benchmark will be updated soon.
```
| Profiles Processed | Likes Given | Comments Given | Pattern | Time Taken |
| -------- | -------- | -------- | -------- | -------- |
| 150 | 418 | 48 | 1C3L3L3L | 10 Hours |
| 125 | 182 | 33 | 1C2L2L2L2L | 4.5 Hours|
```

# Features 
## Profile Mode:
#### 1. Scrape recent 100 followers from a given profile ()
#### 2. Visit each follower and give them like on their 3 most recent posts.
#### 3. Give one comment after 9 likes
#### 4. Repeat for all followers scraped from profile.

## Hash Mode:
#### 1. Scrape 150 (approx +/- 20) recent posts from a given hashtag ( #abcxyz )
#### 2. Visit each post and give a like
#### 3. Give one comment after 9 likes
#### 4. Repeat for all posts scraped from hash tag page.


# Bot Configration 
#### Configurations are stored in 4 files:
| File | Explanation |
| -------- | -------- |
| part_one.txt | Contains first part of comment
| part_to.txt | Contains second part of comment
| em.txt | Contains emoji
- Note: All entries in txt files must be on individual lines.
- Final Comment = Part One + Part Two + Emoji

Will update more info soon...
