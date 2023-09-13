import yt_dlp
import subprocess

def search_and_stream_audio(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'force_generic_extractor': True,
        'extractor_args': ['--no-check-certificate'],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'default_search': 'ytsearch',  # Set the default search provider to YouTube
    }

    try:
        # Create a YoutubeDL instance for searching
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_results = ydl.extract_info(query, download=False)
            if 'entries' in search_results:
                # Get the first video result from the search
                first_video = search_results['entries'][0]
                audio_url = first_video['url']

                # Play the audio in the terminal with mpv and display the progress bar
                subprocess.run(['mpv', '--quiet', '--no-terminal', '--osd-bar', audio_url])
            else:
                print("No search results found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    search_query = input("Enter your search query: ")+" song"
    search_and_stream_audio(search_query)

if __name__ == "__main__":
    main()
