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
		return "%(name)s.vtt"
def process_vtt(file_name):
	print('ye old')
if __name__ == '__main__':
	url = 'https://www.youtube.com/watch?v=sCD9zjf_YRU'
	# list_sub(url)
	file_name = download_sub(url)
	process_vtt(file_name)
	client = Wit('WA2GGNG3O5LKUKKYTGQXFVMJFPE533A5')
	resp = client.message('set an alarm tomorrow at 7am')
	print(resp)
