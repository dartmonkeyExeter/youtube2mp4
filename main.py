from pytube import YouTube, Search

def search_and_download(to_search):
    query = f"{to_search}"
    search_results = Search(query).results
    first = search_results[0]
    video_url = f"https://www.youtube.com/watch?v={first.video_id}"
    
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter().first()
    audio_stream.download(output_path="C:\\Users\\aaron\\Desktop\\youtube to mp4 lmao\\OUTPUTFILES")

def main():
    search_term = input("Search Query: ")
    search_and_download(search_term)

if __name__ == "__main__":
    main()