import wx
import wolframalpha
import wikipedia

class MyFrame(wx.Frame):
    def __init__(self):
        # about the GUI window
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size = wx.Size(450,100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Python GUI") 
        panel = wx.Panel(self)
        
        my_sizer= wx.BoxSizer(wx.VERTICAL)
        Label = wx.StaticText(panel,
        label="Hello I am Pyda the python Digital Assistant. How may I help You?")

        my_sizer.Add(Label, 0, wx.ALL,5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL,5)
        panel.SetSizer(my_sizer)
        self.Show()


    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        print('It Worked')

    try:
        # adding the wolframalpha info
        app_id = '8PEWKT-9Y4XEQG5UA'

        #create a client
        client = wolframalpha.Client(app_id)

        result = client.query(input)
        answer = next(result.results).text

        print(answer)
    except:
        # adding the wikipedia info
        #wikipedia.set_lang('es') #using the different languages
        print (wikipedia.summary(input, sentences =2)) # fetch the data from wikipedia


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()