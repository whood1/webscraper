# Saves a type of html tag from entered url to desktop

import requests
from bs4 import BeautifulSoup
from tkinter import *	

class HTML_Downloader(Frame):
	def __init__(self, master=None):
		title_var = IntVar()
		p_var = IntVar()
		h1_var = IntVar()
		url = StringVar()

		vars = [
		title_var,
		p_var,
		h1_var,
		url
		]

		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets(vars)

	def create_widgets(self, vars):

		def download():

			printed_text = ''

			url = vars[3].get()
			downloaded_html = requests.get(url).text
			soup_html = BeautifulSoup(downloaded_html, "html.parser")

			printed_title = ''
			printed_p = ''
			printed_h1 = ''

			if vars[0].get() == 1:
				for x in soup_html.find_all('title'):
					printed_title += x.string + "\n"

			if vars[1].get() == 1:
				for x in soup_html.find_all('p'):
					printed_p += x.text + "\n"

			if vars[2].get() == 1:
				for x in soup_html.find_all('h1'):
					printed_h1 += x.string + "\n"

			printed_text = printed_title  + "\n\n" + printed_h1 + "\n\n" + printed_p
			print(printed_text)


		self.instruction = Label(self, text='Enter a URL and choose an HTML tag')
		self.instruction.pack(side='top')

		self.enter_url = Entry(self, textvariable=vars[3])
		self.enter_url.pack(side='top')

		self.check_box_title = Checkbutton(self, text='<title>', variable=vars[0])
		self.check_box_title.pack(side='bottom')

		self.check_box_p = Checkbutton(self, text='<p>', variable=vars[1])
		self.check_box_p.pack(side='bottom')

		self.check_box_h1 = Checkbutton(self, text='<h1>', variable=vars[2])
		self.check_box_h1.pack(side='bottom')

		self.download_button = Button(self, text='Download', command=download)
		self.download_button.pack(side='bottom')

		self.set_url = Button(text='Set URL')



	



	




	
root = Tk()
gui = HTML_Downloader(root)
gui.master.title("Webscraper 0.0.1")
gui.mainloop()