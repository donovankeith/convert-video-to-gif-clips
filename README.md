# 🎥 convert-video-to-gif-clips 

Python script that converts .mp4 videos to multiple .gif clips.

## Uses

- Grab small looping clips for teaching.
- Pull the best clips from your projects to feature in Capability Decks.
- Extract .gif from reference for Mood Boards.

## Examples

#### [BOX](https://www.youtube.com/watch?v=lX6JcybgDFo) by Bot & Dolly and [GMUNK](https://gmunk.com/BOX)

![Clip from "BOX" by GMUNK and Box & Dolly](https://user-images.githubusercontent.com/4267389/213904341-0a2b40a9-ed59-4588-8993-a80b8e4b9cab.gif)
![Clip from "BOX" by GMUNK and Box & Dolly](https://user-images.githubusercontent.com/4267389/213904343-1a306793-a509-4438-9569-ae27b8f6bc19.gif)

#### [Flying Lotus Music Video](https://vimeo.com/15572863?embedded=true&source=vimeo_logo&owner=469120) by [Beeple](https://www.beeple-crap.com/)

![_flying-lotus_kill-your-coworkers_by-beeple_003](https://user-images.githubusercontent.com/4267389/213904078-02b38e80-151a-4027-8ef2-43e4bd1c1a08.gif)
![_flying-lotus_kill-your-coworkers_by-beeple_011](https://user-images.githubusercontent.com/4267389/213904158-cb62ca1c-04ca-4bea-ab1a-16ac242ab330.gif)


## 👨‍💼 Author(s)

- [Donovan Keith](https://www.donovankeith.com)
- [Chat GPT](https://chat.openai.com)

## 🔧 Requirements

- [Python 3+](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/)

## 💾 Installation

1. Install ffmpeg, you can find detailed instructions [here](https://www.ffmpeg.org/download.html)
2. Clone this repository

```console
git clone https://github.com/your-username/convert-mp4-to-gif-clips.git
```

## 🏁 Quickstart

### ⚠️ Warning

DO NOT USE WITH REALLY LONG VIDEOS

1. Trim long movies down to the sections you're most interested in.

### 📋 Instructions

1. Copy this script into a directory where you want to convert your files.
2. Open terminal and `cd` to the directory.
3. `python3 convert-mp4-to-gif-clips.py -i INPUT.mp4`
4. Navigate to the new `gifs/` directory next to your input file.
5. Use Quick Look (spacebar on Mac) and your up/down arrow keys to quickly audition the clips you want to use.
6. Ctrl+C to copy, then Ctrl+V to paste in Google Slides or your

## Usage

```console
python convert-mp4-to-gif-clips.py -i <input_file> -o <output_file> -spacing <clip_spacing_sec> -duration <clip_duration_sec>
```

### Options

- -i, --input_file: Path to the input video file. Default is 'BOX.mp4'
- -o, --output_file: Path to the output gif file. If not provided, it will save the gif clips to a 'gifs' directory next to the input file.
- -spacing, --clip_spacing: Spacing between clips in seconds. Default is 1 second.
- -duration, --clip_duration: Duration of each clip in seconds. Default is 3 seconds.

### Examples

- Convert 'video.mp4' to gif clips, save the clips in the 'gifs' directory and use the default spacing and duration

```console
python convert-mp4-to-gif-clips.py -i video.mp4
```

- Convert 'video.mp4' to gif clips, save the clips in 'output.gif' and use a spacing of 2 seconds and duration of 5 seconds

```console
python convert-mp4-to-gif-clips.py -i video.mp4 -o output.gif -spacing 2 -duration 5
```

## 🗒️ Note

- The script will validate the input and provide errors with suggestions on how to fix them to the user.
- Spacing should be an int or float value greater that 1/30
- Duration should not exceed 30 as the .gif file will be far too large.
- If the 'gifs' directory doesn't exist it will be created.
- The script will set the width of the gifs to 480 pixels.

## Why?

I teach Motion Design at California Institite of the Arts. It's helpful to breakdown longer animations into shorter clips.
I'm posting this here in case anyone else doing motion design needs to assemble decks/boards featuring the best clips from their own work.

## 💡 Inspiration

![Clip from "BOX" by GMUNK and Box & Dolly](https://user-images.githubusercontent.com/4267389/213904344-fe23a71a-42f6-4a67-9870-6050b053e4cb.gif)
![Clip from "BOX" by GMUNK and Box & Dolly](https://user-images.githubusercontent.com/4267389/213904345-39be9ff1-37f6-4ad7-bd32-cfb826cea472.gif)
![Clip from "BOX" by GMUNK and Box & Dolly](https://user-images.githubusercontent.com/4267389/213904346-18e3d9cc-505c-4896-af45-dc974961f4f3.gif)
![Clip from "BOX" by GMUNK and Box & Dolly](https://user-images.githubusercontent.com/4267389/213904347-26e55456-f83f-473d-b0d2-5f76e2216832.gif)

👆🏻 This project is so incredible that I just had to break it down into a series of 3 second clips so that I could watch each of the transitions over and over again.

![box-clips-in-moodboard](https://user-images.githubusercontent.com/4267389/213904201-82a63398-354a-45e0-a757-9eb0715f2667.png)

## ❓Questions / Support?

USE AT YOUR OWN RISK.

Sorry to say, but I likely won't be able to offer much in the way of support, nor respond to feature requests.
Feel free to add an issue, fork, fix, and pull request. I'll try to integrate when I've got some down time.

## 📚 References

- [GIPHY Engineering | » How to make GIFs with FFMPEG » How to make GIFs with FFMPEG](https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/): Reference for FFmpeg settings.
- [Video Downloader for Vimeo - Chrome Web Store](https://chrome.google.com/webstore/detail/video-downloader-for-vime/cgmcdpfpkoildicgacgldinemhgmcbgp/related?hl=en): Useful for grabbing videos from YouTube/Vimeo.

## 🤖 AI Notice

This script & documentation was written in collaboration with ChatGPT.
