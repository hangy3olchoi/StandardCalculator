# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import math


###########################################################################
## Class MyFrame
###########################################################################
class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Standard Calculator", pos = wx.DefaultPosition, size = wx.Size( 353,447 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer1.SetMinSize( wx.Size( 400,490 ) ) 
        self.txt_res = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,50 ), wx.TE_READONLY|wx.TE_RIGHT|wx.NO_BORDER )
        self.txt_res.SetFont( wx.Font( 30, 70, 90, 90, False, "Consolas" ) )
        self.txt_res.SetBackgroundColour( wx.Colour( 242, 242, 242 ) )
        
        bSizer1.Add( self.txt_res, 0, wx.ALL, 5 )
        
        gSizer1 = wx.GridSizer( 7, 4, 0, 0 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button4.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button4, 0, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button5.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button5, 0, wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button6.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button6, 0, wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"←", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button7.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button7, 0, wx.ALL, 5 )
        
        self.m_button8 = wx.Button( self, wx.ID_ANY, u"¹/x", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button8.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button8, 0, wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button9.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button9, 0, wx.ALL, 5 )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, u"²√x", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button10.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button10, 0, wx.ALL, 5 )
        
        self.m_button11 = wx.Button( self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button11.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button11, 0, wx.ALL, 5 )
        
        self.m_button12 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button12.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button12, 0, wx.ALL, 5 )
        
        self.m_button13 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button13.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button13, 0, wx.ALL, 5 )
        
        self.m_button14 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button14.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button14, 0, wx.ALL, 5 )
        
        self.m_button15 = wx.Button( self, wx.ID_ANY, u"×", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button15.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button15, 0, wx.ALL, 5 )
        
        self.m_button16 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button16.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button16, 0, wx.ALL, 5 )
        
        self.m_button17 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button17.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button17, 0, wx.ALL, 5 )
        
        self.m_button18 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button18.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button18, 0, wx.ALL, 5 )
        
        self.m_button19 = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button19.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button19, 0, wx.ALL, 5 )
        
        self.m_button20 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button20.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button20, 0, wx.ALL, 5 )
        
        self.m_button21 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button21.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button21, 0, wx.ALL, 5 )
        
        self.m_button22 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button22.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button22, 0, wx.ALL, 5 )
        
        self.m_button23 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button23.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button23.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer1.Add( self.m_button23, 0, wx.ALL, 5 )
        
        self.m_button24 = wx.Button( self, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button24.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button24.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button24, 0, wx.ALL, 5 )
        
        self.m_button25 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button25.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button25.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button25, 0, wx.ALL, 5 )
        
        self.m_button26 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button26.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button26.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button26, 0, wx.ALL, 5 )
        
        self.m_button27 = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button27.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button27.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.m_button27.SetBackgroundColour( wx.Colour( 137, 185, 220 ) )
        
        gSizer1.Add( self.m_button27, 0, wx.ALL, 5 )
        
        self.m_button251 = wx.Button( self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button251.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button251.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button251, 0, wx.ALL, 5 )
        
        self.m_button261 = wx.Button( self, wx.ID_ANY, u")", wx.DefaultPosition, wx.Size( 80,45 ), 0|wx.NO_BORDER )
        self.m_button261.SetFont( wx.Font( 15, 70, 90, 90, False, "Consolas" ) )
        self.m_button261.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        gSizer1.Add( self.m_button261, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button4.Bind( wx.EVT_BUTTON, self.btnPercent )
        self.m_button5.Bind( wx.EVT_BUTTON, self.btnClearEntry )
        self.m_button6.Bind( wx.EVT_BUTTON, self.btnClear )
        self.m_button7.Bind( wx.EVT_BUTTON, self.btnBackspace )
        self.m_button8.Bind( wx.EVT_BUTTON, self.btnQuickDivide )
        self.m_button9.Bind( wx.EVT_BUTTON, self.btnQuickSquare )
        self.m_button10.Bind( wx.EVT_BUTTON, self.btnQuickRootSquare )
        self.m_button11.Bind( wx.EVT_BUTTON, self.btnDivide )
        self.m_button12.Bind( wx.EVT_BUTTON, self.btnSeven )
        self.m_button13.Bind( wx.EVT_BUTTON, self.btnEight )
        self.m_button14.Bind( wx.EVT_BUTTON, self.btnNine )
        self.m_button15.Bind( wx.EVT_BUTTON, self.btnMultiple )
        self.m_button16.Bind( wx.EVT_BUTTON, self.btnFour )
        self.m_button17.Bind( wx.EVT_BUTTON, self.btnFive )
        self.m_button18.Bind( wx.EVT_BUTTON, self.btnSix )
        self.m_button19.Bind( wx.EVT_BUTTON, self.btnMinus )
        self.m_button20.Bind( wx.EVT_BUTTON, self.btnOne )
        self.m_button21.Bind( wx.EVT_BUTTON, self.btnTwo )
        self.m_button22.Bind( wx.EVT_BUTTON, self.btnThree )
        self.m_button23.Bind( wx.EVT_BUTTON, self.btnPlus )
        self.m_button24.Bind( wx.EVT_BUTTON, self.btnSignChange )
        self.m_button25.Bind( wx.EVT_BUTTON, self.btnZero )
        self.m_button26.Bind( wx.EVT_BUTTON, self.btnPoint )
        self.m_button27.Bind( wx.EVT_BUTTON, self.btnEquals )
        self.m_button251.Bind( wx.EVT_BUTTON, self.btnLeftParenthesis )
        self.m_button261.Bind( wx.EVT_BUTTON, self.btnRightParenthesis )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def btnPercent( self, event ):
        res = (float)(self.txt_res.GetValue())/100
        self.txt_res.SetValue(str(res))
                    
        event.Skip()
    
    def btnClearEntry( self, event ):
        self.txt_res.Clear()
        
        event.Skip()
    
    def btnClear( self, event ):
        self.txt_res.Clear()
        
        event.Skip()
    
    def btnBackspace( self, event ):
        res = self.txt_res.GetValue()
        self.txt_res.Clear()
        
        self.txt_res.SetValue(res[:-1])
                
        event.Skip()
    
    def btnQuickDivide( self, event ):
        try:
            res = 1/(int)(self.txt_res.GetValue())
            self.txt_res.SetValue(str(res))
        
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
                    
        event.Skip()
    
    def btnQuickSquare( self, event ):
        try:
            res = ((int)(self.txt_res.GetValue()))*(int)(self.txt_res.GetValue())
            self.txt_res.SetValue(str(res))
        
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
            
        event.Skip()
    
    def btnQuickRootSquare( self, event ):
        try:
            res = math.sqrt((float)(self.txt_res.GetValue()))
            self.txt_res.SetValue(str(res))
        
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
            
        event.Skip()
    
    def btnDivide( self, event ):
        self.txt_res.AppendText("/")
        
        event.Skip()
    
    def btnSeven( self, event ):
        self.txt_res.AppendText("7")
        
        event.Skip()
    
    def btnEight( self, event ):
        self.txt_res.AppendText("8")
        event.Skip()
    
    def btnNine( self, event ):
        self.txt_res.AppendText("9")
        
        event.Skip()
    
    def btnMultiple( self, event ):
        self.txt_res.AppendText("*")
        
        event.Skip()
    
    def btnFour( self, event ):
        self.txt_res.AppendText("4")
        
        event.Skip()
    
    def btnFive( self, event ):
        self.txt_res.AppendText("5")
        
        event.Skip()
    
    def btnSix( self, event ):
        self.txt_res.AppendText("6")
        
        event.Skip()
    
    def btnMinus( self, event ):
        self.txt_res.AppendText("-")
        
        event.Skip()
    
    def btnOne( self, event ):
        self.txt_res.AppendText("1")
        
        event.Skip()
    
    def btnTwo( self, event ):
        self.txt_res.AppendText("2")
        
        event.Skip()
    
    def btnThree( self, event ):
        self.txt_res.AppendText("3")
        
        event.Skip()
    
    def btnPlus( self, event ):
        self.txt_res.AppendText("+")
        
        event.Skip()
    
    def btnSignChange( self, event ):
        try:        
            res = -((int)(self.txt_res.GetValue()))
            self.txt_res.SetValue(str(res))
            
        except:
            res = 'error!'
            self.txt_res.SetValue(res)        
        
        event.Skip()
    
    def btnZero( self, event ):
        self.txt_res.AppendText("0")
        
        event.Skip()
    
    def btnPoint( self, event ):
        self.txt_res.AppendText(".")
        
        event.Skip()
    
    def btnEquals( self, event ):
        try:
            res = eval(self.txt_res.GetValue())
            self.txt_res.SetValue(str(res))
        
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
        
        event.Skip()
    
    def btnLeftParenthesis( self, event ):
        self.txt_res.AppendText("(")
        
        event.Skip()
    
    def btnRightParenthesis( self, event ):
        self.txt_res.AppendText(")")
        
        event.Skip()
    
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent = None)
    frame.Show()
    app.MainLoop()  
