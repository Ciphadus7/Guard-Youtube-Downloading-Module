from pytube import YouTube

#Download Query Loop

while True:
    #Enter URL of the Video
    print("Please enter the URL of the video that you wish to download: ")
    url = input()

    urlInput = YouTube(url)

    #Get The Title
    print("==========Video Title==========")
    print(urlInput.title)


    #Get Available Stream Resoultions
    print("==========Resoultion Options==========")
    optionalStreams = urlInput.streams

    for stream in optionalStreams:
        print(stream)

    #Choose itag for the download resoultion
    print("==========Itag Entry==========")
    print("Please choose any 'itag' from above and enter the corresponding number to begin your download.")
    stream = urlInput.streams.get_by_itag(input())
    stream.download()

    print("Downloaded")
    print("Would you like to download any more videos?")
    answer = input()
    #Loop to decide whether more videos are to be downloaded or is the program to be terminated.
    if answer == 'yes':
        continue
    else:
        break
