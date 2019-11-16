Sub Letter2Colors_MyVersion()
' This is a modified version of Letter2Colors_Synesthesia created by Olympia Colizoli and Nick Daems
' Modified to use the median colorset of 6588 synesthetes, as found by Witthoft, Winawer, and Eagleman (2015)

' Letter2Colors
' Simple search and replace


'        A : red
'        B : blue
'        C : yellow
'        D : blue
'        E : green
'        F : green
'        G : green
'        H : orange
'        I : white
'        J : orange
'        K : orange
'        L : yellow
'        M : red
'        N : orange
'        O : white
'        P : purple
'        Q : purple
'        R : red
'        S : yellow
'        T : blue
'        U : orange
'        V : purple
'        W : blue
'        X : black
'        Y : yellow
'        Z : black

''''''
    Dim red As Long
    Dim orange As Long
    Dim yellow As Long
    Dim green As Long
    Dim blue As Long
    Dim purple As Long
    Dim white As Long
    Dim black As Long

    
    red = RGB(255, 0, 0)
    orange = RGB(255, 128, 0)
    yellow = RGB(255, 255, 0)
    green = RGB(0, 255, 0)
    blue = RGB(0, 0, 255)
    purple = RGB(255, 0, 255)
    white = RGB(0, 0, 0)
    black = RGB(255, 255, 255)


    Dim a_color As Long
    Dim b_color As Long
    Dim c_color As Long
    Dim d_color As Long
    Dim e_color As Long
    Dim f_color As Long
    Dim g_color As Long
    Dim h_color As Long
    Dim i_color As Long
    Dim j_color As Long
    Dim k_color As Long
    Dim l_color As Long
    Dim m_color As Long
    Dim n_color As Long
    Dim o_color As Long
    Dim p_color As Long
    Dim q_color As Long
    Dim r_color As Long
    Dim s_color As Long
    Dim t_color As Long
    Dim u_color As Long
    Dim v_color As Long
    Dim w_color As Long
    Dim x_color As Long
    Dim y_color As Long
    Dim z_color As Long


    a_color = red
    b_color = blue
    c_color = yellow
    d_color = blue
    e_color = green
    f_color = green
    g_color = green
    h_color = orange
    i_color = white
    j_color = orange
    k_color = orange
    l_color = yellow
    m_color = red
    n_color = orange
    o_color = white
    p_color = purple
    q_color = purple
    r_color = red
    s_color = yellow
    t_color = blue
    u_color = orange
    v_color = purple
    w_color = blue
    x_color = black
    y_color = yellow
    z_color = black
    
    
	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[aA]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = a_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[bB]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = b_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[cC]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = c_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[dD]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = d_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[eE]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = e_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[fF]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = f_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[gG]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = g_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[hH]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = h_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[iI]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = i_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[jJ]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = j_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[kK]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = k_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[lL]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = l_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[mM]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = m_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[nN]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = n_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[oO]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = o_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[pP]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = p_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[qQ]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = q_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[rR]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = r_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[sS]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = s_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[tT]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = t_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[uU]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = u_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[vV]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = v_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[wW]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = w_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[xX]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = x_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[yY]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = y_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll


	Selection.Find.ClearFormatting
	Selection.Find.Replacement.ClearFormatting
	With Selection.Find
		.Text = "<[zZ]*>"
		.MatchCase = False
		.Replacement.Text = ""
		.Forward = True
		.Wrap = wdFindContinue
		.Format = True
		.MatchWholeWord = False
		.MatchByte = False
		.CorrectHangulEndings = True
		.MatchWildcards = True
		.MatchSoundsLike = False
		.MatchAllWordForms = False
		.Replacement.Font.Color = z_color
	End With
	Selection.Find.Execute Replace:=wdReplaceAll

End Sub

