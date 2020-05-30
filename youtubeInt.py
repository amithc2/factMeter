import youtube_dl
from wit import Wit

def download_sub(video_url, lang='en'):
	params = {
			"skip_download": True,
			"writesubtitles": "%(name)s.vtt",
            "writeautomaticsub": "auto%(name)s.vtt",
			"subtitlelangs": lang
		}
	with youtube_dl.YoutubeDL(params) as yt:
		yt.download([video_url])

if __name__ == '__main__':
	url = 'https://www.youtube.com/watch?v=sCD9zjf_YRU'
	# list_sub(url)
	download_sub(url)
	client = Wit('WA2GGNG3O5LKUKKYTGQXFVMJFPE533A5')
	resp = client.message('set an alarm tomorrow at 7am')
	print(resp)
