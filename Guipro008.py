import wx

class regexps ( wx.Frame ):
    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent=None, id = wx.ID_ANY, title = u"Data Quality -- Выбор и отладка регулярных"
                            u" выражений", pos = wx.DefaultPosition, size = wx.Size( 510,477 ),
                            style = wx.CAPTION|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

        sizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.regexps_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 ) # Здесь в отличае
        # от предыдущего примера добавлена Self чтобы можно было обратиться из любого метода класса
        self.dq_params_tab = wx.Panel( self.regexps_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL ) # панель которая добавляется на ноутбук, будет площадкой для всех вкладок
        sizer2 = wx.BoxSizer(wx.VERTICAL) # еще один сайзер
        self.use_param_checkbox = wx.CheckBox(self.dq_params_tab, wx.ID_ANY, u"Использовать параметр",
                                              wx.DefaultPosition,
                                              wx.DefaultSize, 0) # добавляем компонент чекбокс на панель dq_params_tab
        sizer2.Add(self.use_param_checkbox, 0, wx.ALL, 5)
        # self.params_quality_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #
        # self.params_choice_pull = wx.Choice(self.dq_params_tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
        #                                     self.params_quality_choices, 0)
        # # Обозначение индекс варианта, который будет выбран изначально после инициализации элемента wx.Choice.
        # self.params_choice_pull.SetSelection(0)

        # Добавлени на вкладку статической линии.
        self.static_line = wx.StaticLine(self.dq_params_tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.LI_HORIZONTAL)

        sizer2.Add(self.static_line, 0, wx.EXPAND | wx.ALL, 5)
        self.static_text = wx.StaticText(self.dq_params_tab, wx.ID_ANY, u"Ввод весового коэффициента",
                                         wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        sizer2.Add(self.static_text, 0, wx.ALL, 5)
        self.weights_txt = wx.TextCtrl(self.dq_params_tab)
        sizer2.Add(self.weights_txt, 0, wx.ALL, 5)

        self.dq_params_tab.SetSizer(sizer2)
        self.dq_params_tab.Layout()
        sizer2.Fit(self.dq_params_tab)

        # Добавление вкладки на панель.
        self.regexps_notebook.AddPage(self.dq_params_tab, u"Параметры оценки", False)
        self.regexps_tab = wx.Panel(self.regexps_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        sizer3 = wx.BoxSizer(wx.VERTICAL)

        # regexps_listboxChoices = []
        self.regexps_listbox = wx.ListBox(self.regexps_tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)

        # Объявление грида (wx.grid.Grid). Это каркас таблицы, как в mysql, oracle, sqlite and etc. В опциях указан размер, и наличие скроллов.
        # self.check_grid = wx.grid.Grid(self.check_sql_tab, wx.ID_ANY, wx.DefaultPosition, wx.Size(480, 407),
        #                                wx.HSCROLL | wx.VSCROLL)

        # Создание непосредственно грида, количества колонок и строк.
        # Grid
        # self.check_grid.CreateGrid(5, 5)

        # Задание свойств грида.
        # self.check_grid.EnableEditing(False)
        # self.check_grid.EnableGridLines(True)
        # self.check_grid.EnableDragGridSize(False)
        # self.check_grid.SetMargins(0, 0)
        #
        # # Задание свойств колонок
        # # Columns
        # self.check_grid.EnableDragColMove(False)
        # self.check_grid.EnableDragColSize(False)
        # self.check_grid.SetColLabelSize(20)
        # self.check_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Свойства строк.
        # Rows
        # self.check_grid.AutoSizeRows(True)
        # self.check_grid.EnableDragRowSize(True)
        # self.check_grid.SetRowLabelSize(40)
        # self.check_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

ex = wx.App()
regexps(None, 'NoteBook demo')
ex.MainLoop()