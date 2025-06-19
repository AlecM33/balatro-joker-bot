# balatro-joker-bot
A Reddit bot that monitors a subreddit and replies with Balatro info to Reddit comments that contain a Balatro Joker/Tarot Card/Spectral Card/Planet Card/Voucher/Blind in double square brackets. Inspired by u/balatro-bot.

The bot uses PRAW's [Subreddit stream](https://praw.readthedocs.io/en/stable/code_overview/other/subredditstream.html) feature to observe and reply to comments in nearly real-time. It uses fuzzy string matching via Levenshtein distance to get the closest Joker/Tarot/etc. and remove the need for exact spelling.

I sourced the information from Balatro's files and version controlled it here to avoid any web scraping. The bot still provides a link to https://balatrowiki.org/ for a given item, so users can see an image and an expanded description.

With the comment stream, a main concern is rate limiting. Reddit allows 1000 requests/10 min. So far when spectating r/balatro with the bot I have not seen the remaining quota dip below 800 or so, so hopefully that will be more than enough for a while.

![image](https://github.com/user-attachments/assets/b97e9567-ceaa-4535-b97f-c9457dedf194)

