"""convert-mp4-to-gif-clips.py
Converts a .mp4 video to a series of short .gif clips.
"""

import os
import subprocess
import argparse
import re
import copy

def get_video_duration_in_sec(video_path):
    """Convert video at `video_path` """

    cmd = ['ffmpeg', '-i', video_path]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()

    matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", output, re.DOTALL).groupdict()

    hours = int(matches['hours'])
    minutes = int(matches['minutes'])
    seconds = float(matches['seconds'])
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds

    return total_seconds


def convert_video_to_gif_clips(input_file, output_file, spacing_sec=3, duration_sec=3, width_px=480):
    width_px = int(width_px)
    video_dur_sec = get_video_duration_in_sec(input_file)
    total_clip_count = int(video_dur_sec / duration_sec)

    #set the start time for the first subclip
    start_sec = 0

    #create a counter for naming the gifs
    counter = 1

    #loop through the video, creating subclips
    while start_sec < video_dur_sec:
        print(f'[{counter}/{total_clip_count}] Converting {start_sec}-{min(start_sec+duration_sec, video_dur_sec)}')

        # Reference
        # https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/
        subprocess.call([
            "ffmpeg",
            "-ss", str(start_sec),
            "-t", str(duration_sec),
            "-i", input_file,
            "-filter_complex", f"[0:v] fps=12,scale={width_px}:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse",
            output_file[:-4] + f"_{counter:03}" + '.gif'
        ]
        )

        #increment the start time for the next subclip
        start_sec += spacing_sec

        #increment the counter for naming the gifs
        counter += 1

def infer_output_filename(input_file):
    dir_name = os.path.dirname(input_file)
    filename_base = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(dir_name, "gifs", filename_base + ".gif")

    return output_file

def validate_input(args):
    args = copy.deepcopy(args)

    if not os.path.isfile(args.input_file):
        raise ValueError(f'{args.input_file} is not a valid file')

    if not re.search(r'\.mp4$', args.input_file):
        raise ValueError(f'{args.input_file} is not a valid video file, it should be an mp4 file')

    if args.output_file is None:
        args.output_file = infer_output_filename(args.input_file)
        print("Output file not specified, defaulting to " + args.output_file)

    if not os.path.exists(os.path.dirname(args.output_file)):
        os.makedirs(os.path.dirname(args.output_file))
        print(f"Creating directory {os.path.dirname(args.output_file)}")

    if args.clip_spacing < 1/30:
        raise ValueError(f'Spacing should be greater than {1/30}')

    if args.clip_duration > 30:
        raise ValueError(f'Duration should not exceed 30 seconds')

    return args

if __name__ == "__main__":
    print("Convert *.mp4 Videos to *.gif Clips")

    parser = argparse.ArgumentParser(description='Dummy script that prints the input given by the user')
    parser.add_argument('-i', '--input_file', help='Input file with .mp4 extension', required=True)
    parser.add_argument('-o', '--output_file', help='Output file with .gif extension')
    parser.add_argument('-spacing', '--clip_spacing', help='Spacing between clips in seconds', type=float, default=1)
    parser.add_argument('-duration', '--clip_duration', help='Clip duration in seconds', type=int, default=3)
    parser.add_argument('-w', '--width', help='Width in pixels', type=int, default=480)
    args = parser.parse_args()

    try:
        args = validate_input(args)
    except ValueError as e:
        print(e)
        exit(1)
    
    print(f'Input file: {args.input_file}')
    print(f'Output file: {args.output_file}')
    print(f'Spacing between clips: {args.clip_spacing} seconds')
    print(f'Clip duration: {args.clip_duration} seconds')
    print(f'Output width: {args.width} px')

    convert_video_to_gif_clips(args.input_file, args.output_file, args.clip_spacing, args.clip_duration, args.width)