import PySimpleGUI as sg
from pytube import YouTube

sg.theme('DarkAmber')

layout = [
    [sg.Titlebar('Download do Youtube')],
    [sg.Text('Cole a URL do Vídeo')],
    [sg.Input(size=(50,1), key='url')],
    [sg.Button('Download')]
]

window = sg.Window('window', layout)

while True:
    event, values = window.read(timeout=10000) # lê eventos com um timeout de 100ms

    # se o timeout expirou ou o usuário fechou a janela, encerra o programa
    if event is None or event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Download':
        link = window['url'].get()
        video = YouTube(link)
        stream = video.streams.get_highest_resolution().download()

    # se o download estiver concluído, fecha a janela
    if stream.is_finished:
        window.close()

# fecha a janela se ela ainda estiver aberta
window.close()

print('Download completado!')
