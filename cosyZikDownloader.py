import discord
import asyncio
import re
import youtube_dl
import sys

ALAIZE = "395395438003355650"
CHAN_SON = "409845505431044096"

client = discord.Client()

ydl_opts = {
    'format': 'best',
    'forcefilename' : True
}

ydl_opts_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	server = client.get_server(ALAIZE)
		
	print(server.id, server)
	channel = server.get_channel(CHAN_SON)
	print(channel)
	
	async for message in client.logs_from(channel, limit=limit):

		searchUrl = re.search(r"(?P<url>https?://www\.youtube\.[^\s]+)", message.content)
		if searchUrl:
			youtubeURL = searchUrl.group("url")
			try:
				options = ydl_opts
				if mode != 0:
					options = ydl_opts_mp3
				with youtube_dl.YoutubeDL(options) as ydl:
					ydl.download([youtubeURL])

			except:
				pass

	await client.logout()

if __name__ == "__main__":
	login = sys.argv[1]
	password = sys.argv[2]
	limit = 100
	if len(sys.argv) >= 4:
		limit = int(sys.argv[3])

	mode = 0
	if len(sys.argv) >= 5:
		mode = int(sys.argv[4])

	print("Using a limit of", limit, "messages")
	if mode != 0:
		print("Conversion to MP3 enabled")

	client.run(login, password, loop = False)

