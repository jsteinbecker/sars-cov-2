joshsteinbecker@Joshs-MacBook-Pro jts_project % 

 Session contents restored from 3/8/2022 at 7:10:25 PM 

joshsteinbecker@Joshs-MacBook-Pro jts_project % pandoc -f html -t markdown jts_schedule.html
::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    import numpy as np

    """SCHEME
    GRID AXIS 0: EMPLOYEE
    GRID AXIS 1: DATE
    e for EMPLOYEE_ID
    d for DATE_ID
    s for SHIFT_ID

    0 is a cell that hasnt been assigned.
    1:8 are different shifts
    -1 is paid time off (pto)
    """
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[ \]:
:::

::: {.jp-RenderedText .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/plain"}
    'SCHEME\nGRID AXIS 0: EMPLOYEE\nGRID AXIS 1: DATE\ne for EMPLOYEE_ID\nd for DATE_ID\ns for SHIFT_ID\n\n0 is a cell that hasnt been assigned.\n1:8 are different shifts\n-1 is paid time off (pto)\n'
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    grid = np.zeros((14,14))
    grid[0][0:4] = -1
    grid[1][4:11] = 8
    grid[2][4:11] = 7
    grid[6][3:11] = 3
    grid [7][5:7] = -1
    grid
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[ \]:
:::

::: {.jp-RenderedText .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/plain"}
    array([[-1., -1., -1., -1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  7.,  7.,  7.,  7.,  7.,  7.,  7.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  3.,  3.,  3.,  3.,  3.,  3.,  3.,  3.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0., -1., -1.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
             0.]])
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def employeeview (empID):
       return grid[empID]
    def dayview (dayID):
       d = grid.transpose()
       return d[dayID]
    dayview(7)[8]
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[ \]:
:::

::: {.jp-RenderedText .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/plain"}
    0.0
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """
    Check Week: Verify not more than 4 shifts (40 hrs)
    per week.
    """
    def week1count (e):
       count = 0
       emp1w = grid[e][0:7]
       for x in emp1w:
          if x != 0:
             count += 1
       return count
    def week2count (e):
       count = 0
       emp1w = grid[e][7:14]
       for x in emp1w:
          if x != 0:
             count += 1
       return count
    def checkweek (e,d):
       if d < 7:
          if week1count(e) < 5:
            return True
       if d > 6:
          if week2count(e) < 5:
             return True
          else:
             return False
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """Checking FTE
    Verify each employee is not assigned higer than their fte"""
    def countEmpShifts (empID):
       view = employeeview(empID)
       count = 0
       for x in view:
          if x > 0 or x == -1:
             count += 1
       return count
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedText .jp-OutputArea-output mime-type="text/plain"}
    The history saving thread hit an unexpected error (OperationalError('database or disk is full')).History will not be written to the database.
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    empFTE = [7,7,8,7,8,8,8,7,8,8,5,5,8,8] # FTE Shifts for each employee
    def notUnderFTE (e):
       if AllEmpCount()[e] < empFTE[e]:
          return True
       # for x in range(len(s)):
       #    if s[x] <= empFTE[x]:
       #       return True
       return False
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """Verify the assigned employee is trained for the
    assigned shift"""

    trainedfor = [[0,1,2,3,4,5,6,7,8], 
                  [0,1,2,3,4,5,6,7,8],
                  [5,6,7,8],
                  [5,6,7,8],
                  [3,5,8],
                  [0,1,2,3,4,5,6,7,8],
                  [3],
                  [0,1,2,4,5,6,7,8],
                  [1,2],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8]]
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """Verify the assigned employee is trained for the
    assigned shift"""

    trainedfor = [[0,1,2,3,4,5,6,7,8], 
                  [0,1,2,3,4,5,6,7,8],
                  [5,6,7,8],
                  [5,6,7,8],
                  [3,5,8],
                  [0,1,2,3,4,5,6,7,8],
                  [3],
                  [0,1,2,4,5,6,7,8],
                  [1,2],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8]]
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    grid[[5]]
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[ \]:
:::

::: {.jp-RenderedText .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/plain"}
    array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def isTrainedFor ():
       val = []
       celllist = []
       for e in range(9):
          for x in employeeview(e):
             if x > 0:
                if x in trainedfor[e]:
                   val.append("T")
                else:
                   cell = f'emp={e},s={x}'
                   celllist.append(cell)
                   val.append("F")
             if x == 0:
                val.append("T")
       if val.count('F') == 0:
          return True
       else:
          return False, celllist
    print(isTrainedFor())
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedText .jp-OutputArea-output mime-type="text/plain"}
    True
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def countDayShifts (dayID):
       view = dayview(dayID)
       count = 0
       for x in view:
          if x > 0:
             count += 1
       return count
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def emptrained (e,s):
       if s in trainedfor[e]:
          return True
       else:
          return False
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def isTrainedFor ():
       val = []
       celllist = []
       for e in range(9):
          for x in employeeview(e):
             if x > 0:
                if x in trainedfor[e]:
                   val.append("T")
                else:
                   cell = f'emp={e},s={x}'
                   celllist.append(cell)
                   val.append("F")
             if x == 0:
                val.append("T")
       if val.count('F') == 0:
          return True
       else:
          return False, celllist
    print(isTrainedFor())
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedText .jp-OutputArea-output mime-type="text/plain"}
    True
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def countDayShifts (dayID):
       view = dayview(dayID)
       count = 0
       for x in view:
          if x > 0:
             count += 1
       return count
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def cellswithShifts():
       count = 0
       for x in grid:
          for y in x:
             if y != 0:
                count += 1
       return count
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def shiftnotonday (d,s):
       if s in dayview(d):
          return False
       return True
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def shiftnotonday (d,s):
       if s in dayview(d):
          return False
       return True
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """Verifys an evening shift does not directly 
    proceed a morning shift"""

    def noturnaround(e,d,s):
       if s>5 and d !=13:
          if grid[e][d+1] != 0:
             if grid[e][d+1] < 5:
                return False
       if s<4 and d !=0:
          if grid[e][d-1] !=0:
             if grid[e][d-1] > 5:
                return False
       return True
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def solveCell (d,e,s):
       x = emptrained(e,s)
       y = notUnderFTE(e)
       z = shiftnotonday(d,s)
       m = checkweek(e,d)
       n = noturnaround(e,d,s)
       if x == True:
          if y == True:
             if z == True:
                if m == True:
                   if n == True:
                      grid[e][d]=s
       return False
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    for x in grid.transpose():
       y = np.setxor1d(range(9),x)
       z = np.intersect1d(y,range(9))
       z
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def AllEmpCount ():
       callEmpCount = []
       for x in range(14):
          c = countEmpShifts(x)
          callEmpCount.append(c)
       return callEmpCount
    AllEmpCount()
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[ \]:
:::

::: {.jp-RenderedText .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/plain"}
    [4, 7, 7, 0, 0, 0, 8, 2, 0, 0, 0, 0, 0, 0]
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """Verifys an evening shift does not directly 
    proceed a morning shift"""

    def noturnaround(e,d,s):
       if s>5 and d !=13:
          if grid[e][d+1] != 0:
             if grid[e][d+1] < 5:
                return False
       if s<4 and d !=0:
          if grid[e][d-1] !=0:
             if grid[e][d-1] > 5:
                return False
       return True
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    def solveCell (d,e,s):
       x = emptrained(e,s)
       y = notUnderFTE(e)
       z = shiftnotonday(d,s)
       m = checkweek(e,d)
       n = noturnaround(e,d,s)
       if x == True:
          if y == True:
             if z == True:
                if m == True:
                   if n == True:
                      grid[e][d]=s
       return False
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    """Run 20000 iterations of random possible shift assignments"""

    x = 0
    while x < 20000:
       d =np.random.randint(0,14)
       e = np.random.randint(0,14)
       s = np.random.randint(0,9)
       if grid[e][d] == 0 and notUnderFTE(e) == True and noturnaround(e,d,s) == True:
          #print (grid[e][d],e,d,s,shiftnotonday(d,s),notUnderFTE(e))
          solveCell(d,e,s)
          x +=1
       else:
          x +=1
    print(AllEmpCount(),cellswithShifts())
    print(grid)
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedText .jp-OutputArea-output mime-type="text/plain"}
    [7, 7, 8, 7, 7, 8, 8, 7, 8, 8, 5, 5, 8, 8] 101
    [[-1. -1. -1. -1.  0.  0.  0.  0.  0.  1.  0.  3.  8.  0.]
     [ 0.  0.  0.  0.  8.  8.  8.  8.  8.  8.  8.  0.  0.  0.]
     [ 0.  0.  0.  0.  7.  7.  7.  7.  7.  7.  7.  6.  0.  0.]
     [ 0.  7.  0.  7.  6.  0.  6.  0.  0.  5.  5.  0.  7.  0.]
     [ 5.  0.  0.  8.  5.  0.  0.  5.  0.  0.  0.  5.  3.  8.]
     [ 0.  3.  1.  0.  0.  0.  4.  6.  6.  0.  2.  0.  5.  1.]
     [ 0.  0.  0.  3.  3.  3.  3.  3.  3.  3.  3.  0.  0.  0.]
     [ 4.  0.  5.  4.  0. -1. -1.  0.  0.  4.  0.  2.  0.  0.]
     [ 2.  1.  0.  1.  2.  0.  2.  0.  1.  0.  0.  1.  1.  0.]
     [ 8.  0.  0.  2.  4.  1.  5.  2.  0.  0.  6.  0.  0.  6.]
     [ 0.  0.  8.  6.  0.  0.  0.  0.  5.  2.  0.  0.  2.  0.]
     [ 3.  0.  2.  0.  1.  0.  0.  0.  0.  0.  1.  0.  0.  2.]
     [ 7.  5.  3.  5.  0.  2.  0.  1.  0.  0.  0.  7.  0.  7.]
     [ 1.  8.  6.  0.  0.  5.  1.  4.  2.  0.  0.  8.  0.  0.]]
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: jp-Cell-inputWrapper
::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.CodeMirror .cm-s-jupyter}
::: {.highlight .hl-python}
    print("NCMC CPHT SCHEDULE | 2 WEEK")
    print("-"*60)
    new = ""
    for i in range(len(grid)):
       myrow = ""
       for x in grid[i]:
          if x == 8:
             myrow += "N  "
          if x == 7:
             myrow += "3  "
          if x== 6:
             myrow += "EP "
          if x == 5:
             myrow += "EI "
          if x == 4:
             myrow += "S  "
          if x == 3:
             myrow += "7P "
          if x == 2:
             myrow += "7C "
          if x == 1:
             myrow += "MI "
          if x == 0:
             myrow += ".  "
          if x == -1:
             myrow += "pto"
       myrow += "| EMPLOYEE_NAME"
       new += myrow + "\n"
    new += "-"*65

    print(new)
    print(cellswithShifts())
:::
:::
:::
:::
:::

::: jp-Cell-outputWrapper
::: {.jp-OutputArea .jp-Cell-outputArea}
::: jp-OutputArea-child
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedText .jp-OutputArea-output mime-type="text/plain"}
    NCMC CPHT SCHEDULE | 2 WEEK
    ------------------------------------------------------------
    ptoptoptopto.  .  .  .  .  MI .  7P N  .  | EMPLOYEE_NAME
    .  .  .  .  N  N  N  N  N  N  N  .  .  .  | EMPLOYEE_NAME
    .  .  .  .  3  3  3  3  3  3  3  EP .  .  | EMPLOYEE_NAME
    .  3  .  3  EP .  EP .  .  EI EI .  3  .  | EMPLOYEE_NAME
    EI .  .  N  EI .  .  EI .  .  .  EI 7P N  | EMPLOYEE_NAME
    .  7P MI .  .  .  S  EP EP .  7C .  EI MI | EMPLOYEE_NAME
    .  .  .  7P 7P 7P 7P 7P 7P 7P 7P .  .  .  | EMPLOYEE_NAME
    S  .  EI S  .  ptopto.  .  S  .  7C .  .  | EMPLOYEE_NAME
    7C MI .  MI 7C .  7C .  MI .  .  MI MI .  | EMPLOYEE_NAME
    N  .  .  7C S  MI EI 7C .  .  EP .  .  EP | EMPLOYEE_NAME
    .  .  N  EP .  .  .  .  EI 7C .  .  7C .  | EMPLOYEE_NAME
    7P .  7C .  MI .  .  .  .  .  MI .  .  7C | EMPLOYEE_NAME
    3  EI 7P EI .  7C .  MI .  .  .  3  .  3  | EMPLOYEE_NAME
    MI N  EP .  .  EI MI S  7C .  .  N  .  .  | EMPLOYEE_NAME
    -----------------------------------------------------------------
    101
:::
:::
:::
:::
:::
joshsteinbecker@Joshs-MacBook-Pro jts_project % 