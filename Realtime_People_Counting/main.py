import os
from process_videos import run

#python main.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel    

def find_files(directory):
    video_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".mp4", ".avi")):
                video_files.append(os.path.join(root, file))
    return video_files

def execute():
    videos_directory = "videos"
    #videos_directory = "K:/DCIM/100MEDIA"
    #videos_directory = "K:/DCIM/100_BTCF"
    video_files = find_files(videos_directory)
    total_return = 0
    total_dog_return = 0
    total_bicycle_return = 0

    for file_path in video_files:
        video_return, dog_return, bicycle_return = run(file_path)
        total_return += video_return
        total_dog_return += dog_return
        total_bicycle_return += bicycle_return 

    num_videos = len(video_files)
    average_people_per_video = total_return / num_videos if num_videos > 0 else 0

    print("Number of videos scanned:", num_videos)
    print("Total number of people in all the videos:", total_return)
    print("Average number of people per video:", average_people_per_video)
    print("Total number of dogs in all the videos:", total_dog_return)
    print("Total number of bicycles in all the videos:", total_bicycle_return)
    print("Dogs:People Ratio: ", total_dog_return/total_return)
    print("Bicycle:People Ratio: ", total_bicycle_return/total_return)


execute()