# -*- coding: utf-8 -*-
import wx
import wx.xrc

class MyApp(wx.App):
    def OnInit(self):
        self.frame = IMCWindow(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class IMCWindow ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cálculo do IMC - Índice de Massa Corporal", pos = wx.DefaultPosition, size = wx.Size( 500,300 ))
    
        self.SetSizeHints( -1, -1 )

        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer6 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer7 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer8 = wx.BoxSizer(wx.VERTICAL)
        self.sizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.nameLabel = wx.StaticText( self, wx.ID_ANY, u"Nome do Paciente:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.nameLabel.Wrap( -1 )
        self.sizer2.Add( self.nameLabel, flag= wx.EXPAND | wx.ALL, border = 5)

        self.nameTxt = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sizer2.Add(self.nameTxt, flag= wx.EXPAND | wx.ALL, border = 5)

        self.addressLabel = wx.StaticText( self, wx.ID_ANY, u"Endereço Completo:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.addressLabel.Wrap( -1 )
        self.sizer3.Add(self.addressLabel, flag= wx.EXPAND | wx.ALL, border = 5)

        self.addressTxt = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sizer3.Add(self.addressTxt, flag= wx.EXPAND | wx.ALL, border = 5)

        self.weightLabel = wx.StaticText( self, wx.ID_ANY, u"Peso:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.weightLabel.Wrap( -1 )
        self.sizer4.Add(self.weightLabel, flag= wx.ALIGN_LEFT, border = 5)

        self.weightTxt = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sizer4.Add(self.weightTxt, flag= wx.EXPAND | wx.ALL, border = 5)

        self.heightLabel = wx.StaticText( self, wx.ID_ANY, u"Altura:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.heightLabel.Wrap( -1 )
        self.sizer5.Add(self.heightLabel, flag= wx.ALIGN_LEFT, border = 5)

        self.heightTxt = wx.TextCtrl( self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sizer5.Add(self.heightTxt, flag= wx.EXPAND | wx.ALL, border = 5)

        self.calcTxt = wx.TextCtrl(self, wx.ID_ANY, size=(100,100), style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY|wx.TE_RICH2)
        self.sizer6.Add(self.calcTxt, flag= wx.EXPAND | wx.ALL, border = 5)

        self.calcBtn = wx.Button( self, wx.ID_ANY, u"Calcular", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.sizer7.Add(self.calcBtn, flag= wx.EXPAND | wx.ALL, border = 5)

        self.restartBtn = wx.Button( self, wx.ID_ANY, u"Reiniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sizer7.Add(self.restartBtn, flag= wx.EXPAND | wx.ALL, border = 5)

        self.exitBtn = wx.Button( self, wx.ID_ANY, u"Sair", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sizer7.Add(self.exitBtn, flag= wx.EXPAND | wx.ALL, border = 5)

        self.sizer8.Add(self.sizer4,flag= wx.ALL | wx.ALIGN_LEFT, border = 10)
        self.sizer8.Add(self.sizer5,flag= wx.ALL | wx.ALIGN_LEFT, border = 10)

        self.sizer9.Add(self.sizer8,flag= wx.ALL | wx.ALIGN_LEFT, border = 10)
        self.sizer9.Add(self.sizer6,flag= wx.ALL | wx.ALIGN_LEFT, border = 10)

        self.sizer1.Add(self.sizer2,flag= wx.ALL | wx.ALIGN_LEFT, border = 5)
        self.sizer1.Add(self.sizer3,flag= wx.ALL | wx.ALIGN_LEFT, border = 5)
        self.sizer1.Add(self.sizer9,flag= wx.ALL | wx.ALIGN_LEFT, border = 5)
        self.sizer1.Add(self.sizer7,flag= wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border = 5)

        self.SetSizer( self.sizer1 )
        self.Fit()
        self.Layout()
  
        # Connect Events
        self.calcBtn.Bind( wx.EVT_BUTTON, self.calc )
        self.restartBtn.Bind( wx.EVT_BUTTON, self.restart )
        self.exitBtn.Bind( wx.EVT_BUTTON, self.exit )

    def calc( self, event ):
        weight = int(self.weightTxt.Value)
        height = float(self.heightTxt.Value)/100
        imc = weight/(height ** 2)
        self.calcTxt.Value=u'O IMC de %s (%s) é %0.2f' % (self.nameTxt.Value, self.addressTxt.Value, imc)

    def restart( self, event ):
        self.nameTxt.Value=u""
        self.addressTxt.Value=u""
        self.weightTxt.Value=u""
        self.heightTxt.Value=u""
        self.calcTxt.Value

    def exit( self, event ):
      self.Close()

if __name__=="__main__":
    app=MyApp(False)
    app.MainLoop()