import pytube

link = input("Insira a url do video: ")
tube = pytube.YouTube(link)
tube.streams.first().download()
print("Download concluído!", link)