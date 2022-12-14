from vidstream import *
import tkinter as tkinter
import threading
local_ip_addr = socket.gethostbyname(socket.gethostname())
server = streamingserver(local_ip_addr, 7777)
receiver = AudioReceiver(local_ip_addr, 6666)
def startlistening():
	t1 = threading.Thread(target=server.start_server)
	t2 = threading.Thread(target=server.start_server)
	t1.start()
	t2.start()
def startcamerastream():
	camera_client = CameraClient(text_target_ip.get(1.0, "end-1c"), 9999)
	t3 = threading.Thread(target=camera_client.start_stream)
	t3.start()
def startscreensharing():
	screen_client = ScreenShareClient(text_target_ip.get(1.0, "end-1c"), 9999)
	t4 = threading.Thread(target=screen_client.start_stream)
	t4.start()
def startaudiostream():
	audio_sender = AudioSender(text_target_ip.get(1.0, "end-1c"), 8888)
	t5 = threading.Thread(target=audio_sender.start_stream)
	t5.start()
# gui
window = tk.Tk()
window.title("Zoomclone")
window.geometry("300x200")
label_target_ip = tk.Label(window, text="Target ip:")
label_target_ip.pack()
text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()
btn_listen = tk.Button(window, text="Start Listening", width=50, command=startlistening)
btn_listen.pack(anchor=tk.CENTER, expand=True)
btn_camera = tk.Button(window, text="Start camera stream", width=50, command=startcamerastream)
btn_camera.pack(anchor=tk.CENTER, expand=True)
btn_screen = tk.Button(window, text="Start screen stream", width=50, command=startscreensharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)
btn_audio = tk.Button(window, text="Start audio stream", width=50, command=startaudiostream)
btn_audio.pack(anchor=tk.CENTER, expand=True)
window.mainloop()