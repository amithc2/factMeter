import youtube_dl
from wit import Wit
import process_video
from process_video import process_video

def download_sub(video_url, lang='en'):
	params = {
			# "skip_download": True,
			"writeautomaticsub": "auto%(name)s.vtt",
			"writesubtitles": "%(name)s.vtt",
			"subtitlelangs": lang
		}
	with youtube_dl.YoutubeDL(params) as yt:
		info = yt.extract_info(video_url, download=True)
		filename = yt.prepare_filename(info)
		return filename
def process_vtt(file_name):
	print('ye old' + file_name)
if __name__ == '__main__':
	url = 'https://www.youtube.com/watch?v=3qtIp8joCE0&t=72s'
	# list_sub(url)
	file_name = download_sub(url)
	process_vtt(file_name[:-3]+'en.vtt')
	process_video(file_name)
	client = Wit('WA2GGNG3O5LKUKKYTGQXFVMJFPE533A5')
	resp = client.message('set an alarm tomorrow at 7am')
	print(resp)
