result = MsgBox ("Do you want to enter the system?", vbYesNo + vbQuestion, "Acces System")

Select Case result
Case vbYes
    Dim shell
	Set shell = wscript.CreateObject("Shell.Application")
	shell.Open "system\"
	End Sub
Case vbNo
    MsgBox("Returning...")
End Select
