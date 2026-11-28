# Polylogue User Guide

## Read and reply across languages on iPhone, iPad and Mac

# Part I — Getting started

# Chapter 1: Meet Polylogue

Polylogue is an app for Mastodon and compatible servers. Mastodon is a social network made of many independent servers that talk to each other, often called the Fediverse. Your account lives on one server; Polylogue is the window you use it through.

## What you need

- An iPhone or iPad with iOS or iPadOS 18 or later, or a Mac with macOS 15 or later.
- An account on a Mastodon-compatible server, unless you only want to try the demo.

## What Polylogue adds

It translates the posts you read, and lets you write a reply in your own language, check the translation and publish it. Translation uses Apple's Translation framework on your device. AI translation is an optional extra that you set up yourself.

Polylogue's own menus and buttons are in English.

# Chapter 2: Sign in or try the demo

## Sign in

1. Open Polylogue.
2. Under **Your Mastodon server**, enter your server's address, for example `mastodon.social`.
3. Choose **Continue with Mastodon**. Your web browser opens your server's sign-in page.
4. Sign in there and allow Polylogue to use your account.
5. The browser returns you to Polylogue, which opens your Home timeline.

Your password is entered only on your server. Polylogue keeps the access token it receives in the Keychain, and you stay signed in until you sign out.

If you see **Your saved session expired. Please sign in again.**, repeat these steps.

## Try the demo account

Choose **Explore with a demo account** on the sign-in screen to look around with sample posts. Nothing you do is published. To leave, open **Preferences** and choose **Sign Out**.

## Sign out

Open **Preferences** and choose **Sign Out** under **Account**. This removes the token from your device. To withdraw access on the server too, remove Polylogue from the authorized apps in your Mastodon account settings on the web.

# Chapter 3: Find your way around

## The sidebar

| Item | What it shows |
| --- | --- |
| **Notifications** | Mentions, follows, favorites, boosts and more |
| **Explore** | What is trending on your server, and accounts to follow |
| **Search** | People, hashtags and posts |
| **Bookmarks** | Posts you saved |
| **Favorites** | Posts you favorited |
| **Home**, **Local**, **Federated** | Your timelines |
| **Preferences** | Translation, AI, posting defaults and account |

Your name and picture at the bottom of the sidebar open your own profile.

## iPhone, iPad and Mac

On iPad and Mac the sidebar sits beside the content. On iPhone it is its own screen; choose an item, and use the back button to return. When you open a post, profile, hashtag or article, a round back button at the top left returns you to the list.

On Mac you can also open Preferences from the app menu, with `⌘,`.

# Part II — Reading

# Chapter 4: Read your timelines

## The three timelines

- **Home** holds posts and boosts from accounts and hashtags you follow.
- **Local** holds public posts from accounts on your own server.
- **Federated** holds public posts your server knows about, from your server and others. It is your server's view, not everything that exists.

Choose the information button in the toolbar for a reminder of what a timeline contains.

## Refresh and scroll back

While Polylogue is active, the open timeline checks for new posts about once a minute. You can also choose **Refresh** or pull down. Scroll to the end to load older posts.

Some servers turn off their Local or Federated feeds. Polylogue then tells you the server has disabled that feed.

## What a post offers

Under each post are **Reply**, **Boost**, **Favorite**, **Bookmark** and, when the post has a web address, **Share**. Tap the post or its time to open the conversation. Tap the name or picture to open the profile. A small symbol beside the time marks a post that is not fully public.

# Chapter 5: Conversations, warnings, polls and media

## Open a conversation

Tap a post to see it with the posts before it and the replies after it. A server only knows some replies, so another server may show more. An edited post is marked **Edited**.

## Content warnings

A post with a content warning shows only the warning. Choose **Show** to read it and **Hide** to fold it again.

## Sensitive media

Media marked sensitive is covered, both in timeline lists and in conversations. Choose **Sensitive media** to reveal it. In lists, the previews are not loaded until you do.

## Vote in a poll

Select your choice, or several if the poll allows it, and choose **Vote**. Results appear after you vote or when the poll ends. Some polls hide totals until they end.

## Photos and video

Open the conversation to see media at full width and to play video. Tap an image to view it on its own and to translate text in it.

# Chapter 6: Explore and search

## Explore

Explore has four sections: **Posts**, **Hashtags**, **News** and **For You**. They show what your own server reports as trending, and accounts it suggests with a short reason. Choose a hashtag to see its posts, a news item to read it inside Polylogue, or **Follow** beside a suggested account.

A section can be empty if your server has nothing trending or does not offer it.

## Search

Type at least two characters. Results are grouped into **People**, **Hashtags** and **Posts**. Your server decides what can be found. Searching for a full address, such as `@name@server.example`, can find someone on another server. A hashtag in search results opens its web page.

# Part III — Translation

# Chapter 7: Translate posts

## Set your reading language

Open **Preferences** and choose **Reading language** under **Translation**. You can choose Arabic, Chinese, Dutch, English, French, German, Hindi, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Turkish or Ukrainian. Polylogue starts with your device's language.

## Automatic or on request

**Translate timeline posts automatically** is on at first. Posts in other languages are replaced by their translation, with a line saying which language and how it was translated. Turn it off to see a **Translate from…** button under such posts instead.

Choose **Show original** or **Show translation** to switch. Content warnings and poll choices are shown as written.

## When Apple cannot translate a pair

Which languages work depends on Apple's Translation framework on your device, and your device may ask to download a language first.

**Bridge unsupported Apple pairs through English**, on at first, translates into English and then into your language, both on device. Some nuance may be lost. If no route works, you can use AI translation, described in Chapter 9.

Apple Translation does not work in the iOS Simulator.

## Clear cached translations

Polylogue keeps recent translations so they appear again quickly. Choose **Clear Translation Cache** in Preferences to remove them, including image text.

# Chapter 8: Translate text in images

## Translate an image

1. Open the conversation and tap the image.
2. Choose **Translate Image Text**.
3. Polylogue downloads the image, recognizes its text on your device with Apple Vision, and translates it.

Use **Show Detected Text** to check what was recognized, **Copy** to copy the text shown, and **Hide** or **Show** to move the panel out of the way. Results are cached.

## If it fails

**No readable text was found in this image** means nothing was recognized. If Apple cannot translate the language and you have set up AI translation, you can try the provider. Only the recognized text is sent, never the image, and only for public and quiet public posts.

# Chapter 9: Set up AI translation (optional)

You do not need this to use Polylogue. You need your own account and API key with a provider, which may charge you.

## Turn it on

1. In **Preferences**, turn on **Enable AI translation fallback**.
2. Choose a **Provider**: OpenAI, Anthropic, Google Gemini or OpenAI-compatible.
3. Enter your key and choose **Save API Key**.
4. Choose **Load Available Models** and pick one, or type a model name.
5. For OpenAI-compatible services, enter the full HTTPS chat-completions address.

**Provider status** shows **Ready** when everything is in place. Each provider keeps its own key and model. **Remove Key** deletes the key for the selected provider.

## When AI is used

By default Apple Translation comes first, and a **Translate with AI** button appears only when Apple cannot do the job.

- **Automatically use AI for unsupported languages** translates those posts without waiting for you. It becomes available after you have confirmed an AI translation with the current provider.
- **Use AI assistant before Apple Translation** makes AI the first choice.

## What is sent

Only public and quiet public posts and replies. Followers-only and direct posts are never sent.

Polylogue asks you to confirm the first time it sends a post, image text or a reply to a provider. It asks again when you change to another provider, or to another OpenAI-compatible address. After you confirm, it does not ask again for that one. See the [privacy policy](/polylogue/privacy.html).

# Part IV — Writing

# Chapter 10: Write a post

## Compose

1. Open a timeline and choose **New Post**.
2. Write up to 500 characters.
3. Choose the audience, and add a content warning, media or a poll if you like.
4. Choose **Publish**.

## Choose who can see it

| Audience | Who sees the post |
| --- | --- |
| **Public** | Everyone, including public timelines |
| **Quiet Public** | Everyone, but not listed in public timelines |
| **Followers** | Your followers and people you mention |

## Content warnings

Choose **Add Content Warning** and write a short subject. Attached media is then hidden automatically.

## Starting settings and drafts

New posts take their audience, language, sensitive media and warning settings from your server. See **Server Posting Defaults** in Preferences.

If you choose **Cancel**, your text is kept and restored next time, marked **Draft restored**. Only the text is saved, not media, polls or the warning.

# Chapter 11: Reply across languages

## Write, preview, publish

1. Choose **Reply** under a post, or **Reply across languages** in a conversation.
2. The reply starts with the addresses of the author and of everyone the post mentions, except you, so they are notified. Remove any you do not want to include.
3. Write your reply after them, in your reading language. The addresses at the start are not translated.
4. Check **Reply language**. It starts as the language of the post.
5. Choose **Preview**.
6. Compare your original with the translation, and edit the translation as needed.
7. Choose **Publish**.

When the reply language is your reading language, there is no preview and you publish directly. The reply language list also includes Hungarian.

Mastodon keeps one language version of a post. Others see only what you publish; Polylogue keeps your original on your device. Content warnings and poll choices are published exactly as you typed them.

## Which translator is used

Apple Translation is used when it can. If the post you are answering was translated by AI, the same provider and model translate your reply. AI is also used when Apple does not support the pair and you have AI set up.

The first time a reply would go to a provider you have not confirmed, Polylogue asks. Choose **Send and Translate**, or **Cancel** to keep the text on your device.

## Too long after translation

A translation can be longer than your original. Edit it down to 500 characters, or choose **Shorten with AI** if AI made the translation.

## Privacy of replies

A reply keeps the privacy of the conversation. You cannot make a followers-only conversation public. Private replies are never sent to an AI service; if Apple cannot translate one, write it in the other language yourself.

# Chapter 12: Add media and polls

A post can have media or a poll, not both.

## Photos and video

Choose **Add Photos or Video**, then your Photos library or your files. You can attach up to four. Use **Describe this media for accessibility** for each one, and **Mark media as sensitive** if needed. Remove an item with the button beside it.

Large files take longer: Polylogue uploads them when you publish and waits for the server to process them.

## Polls

Choose **Add Poll**, enter two to four choices, and set the duration, from 5 minutes to 7 days. You can **Allow multiple choices** and **Hide totals until the poll ends**. A poll needs post text too.

# Chapter 13: Edit or delete your post

## Edit

Open your post, choose **More**, then **Edit Post**. You can change the text, content warning, sensitive setting and language. Existing media and polls stay as they are. Choose **Save**.

## Delete

Choose **More**, then **Delete Post**, and confirm. This cannot be undone. Other servers may keep copies for a while.

# Part V — People and your account

# Chapter 14: React, save and keep up

## Boost, favorite, bookmark

- **Boost** shares a post with your followers.
- **Favorite** shows appreciation and adds the post to **Favorites**.
- **Bookmark** saves it privately to **Bookmarks**.

Choose the same button again to undo. All three are stored on your server.

## Notifications

Notifications lists mentions, follows, follow requests, favorites, boosts, edits and finished polls. Choose one with a post to open it. Choose **Refresh** to check again.

# Chapter 15: Profiles, muting, blocking and reporting

## View a profile

Tap a name or picture to see the account's description, fields, counts and recent posts. A seal marks a field your server has verified.

## Follow, mute and block

Choose **Follow**; accounts that approve followers show **Requested** until they accept. In the account actions menu:

- **Mute** hides the account and its notifications.
- **Block** removes the follow relationship both ways and hides the account. You are asked to confirm.

## Report

Choose **Report Account** from a profile, or **Report Post** from a conversation. Pick **Spam**, **Illegal content** or **Other**, describe what happened, and choose **Send Report**. For accounts on another server you can also forward the report there. Your server's moderators decide what happens.

# Chapter 16: Edit your profile

Open your profile from the bottom of the sidebar and choose **Edit Profile**. You can change:

- your display name and biography;
- up to four profile fields, such as a website or pronouns;
- **Require approval for new followers**;
- **Show this profile in discovery**;
- **This is an automated account**.

Choose **Save**. Changing your picture or header image is not available in Polylogue; use your server's website.

# Part VI — Settings and help

# Chapter 17: Preferences

| Section | What it holds |
| --- | --- |
| **Translation** | Reading language, automatic translation, bridging through English, clearing the cache |
| **AI Translation Fallback** | Provider, model, API key and when AI is used |
| **Server Posting Defaults** | Audience, language, sensitive media and content warning settings from your server |
| **Account** | Who you are signed in as, your server, and Sign Out |
| **About** | Version and how translated replies are kept |

Server posting defaults are changed on your server's website. Choose **Refresh from Server** to load them again.

# Chapter 18: Privacy and stored data

Polylogue has no account of its own, no ads and no analytics. It connects to your Mastodon server, to the places that host images, video and articles you view, and to an AI provider only if you set one up.

## On your device

Your sign-in token and API keys are in the Keychain. Settings, drafts, your originals of translated replies and translation caches are in the app's storage. Cached translations can include text from private posts, translated on your device.

Signing out does not erase drafts, caches or API keys. Use **Clear Translation Cache** and **Remove Key** if you want them gone.

Read the full [privacy policy](/polylogue/privacy.html).

# Chapter 19: Troubleshoot common problems

## I cannot sign in

Enter just the server address, such as `mastodon.social`. Check that the server opens in your web browser. After allowing access, let the browser open Polylogue.

## Posts are not translated

- Check **Reading language** and that the post is in a different language.
- Accept any language download your device offers.
- Turn on bridging through English.
- For languages Apple does not support, set up AI translation.

## AI translation does not work

Check **Provider status**. Confirm the key, model and, for compatible services, the HTTPS address. An error from the provider is shown under the post. Private and direct posts are never translated by AI.

## A timeline or Explore is empty

Follow some accounts for Home. Local, Federated and Explore depend on what your server offers.

## This server returned data Polylogue could not read

Your server may differ from Mastodon in ways Polylogue does not yet handle. [Tell us](/polylogue/support.html) which server software it runs.

## A post will not publish

Check the 500-character limit, that a poll has two choices and some text, and your connection. Polylogue uses a 500-character limit even if your server allows more.
