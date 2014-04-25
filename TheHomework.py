#! /usr/bin/evn python

import wx, random, time

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		self.i = 0
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Game Start!")
		
		self.panel = wx.Panel(self)
		
		self.btnStart = wx.Button(self.panel, label = "Start Game Here")
		self.btnStart.Bind(wx.EVT_BUTTON, self.OCStart)
		
		self.list = []
		
		for j in range(0, 10):README.md
			temp = wx.Button(self.panel, label = "CLICK HERE!", pos=(random.randint(0,200), random.randint(0,400)))
			temp.Bind(wx.EVT_BUTTON, self.OCbtn)
			temp.Show(False)
			self.list.append(temp)
		
		self.gameOver = wx.StaticText(self.panel, label = 'Game over, your time is')
		self.gameOver.Show(False)
	
	def OCStart(self, e):
		self.btnStart.Show(False)
		self.startTime = time.time()
		self.list[0].Show(True)
	
	def OCbtn(self, e):
		self.list[self.i].Show(False)
		self.i = self.i + 1
		if self.i != 10:
			self.list[self.i].Show(True)
		else:
			self.gameOver.Show(True)
			self.message = wx.StaticText(self.panel, label = str (time.time() - self.startTime) + ' seconds. ', pos=(100, 200))

app = wx.App(False)

frame = TenButtonFrame(None)

frame.Show()

app.MainLoop()
