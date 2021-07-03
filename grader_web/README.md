# KVISOI

- installation
  - clone and install programming.in.th/grader
  - config programming.in.th/grader and this
  - runserver
  - adjust proxy accordingly

TODO :
WS
FrontEnd
Finish post route
POST to grader
DEPLOY Test

# Temp request
# SubmissionID=1 Results:='{"Score":0,"Time":0,"Memory":0,"GroupResults":[{"Score":0,"FullScore":30,"Status":[{"Verdict":"Judge Error","Score":"0","Time":0,"Memory":0,"Message":"Judge killed: internal error"},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""}]}]}'
# SubmissionID=1 Results:='{"Score":0,"Time":0,"Memory":0,"GroupResults":[{"Score":0,"FullScore":30,"Status":[{"Verdict":"Judge Error","Score":"0","Time":0,"Memory":0,"Message":"Judge killed: internal error"},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""}]},{"Score":0,"FullScore":70,"Status":[{"Verdict":"Judge Error","Score":"0","Time":0,"Memory":0,"Message":"Judge killed: internal error"},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""},{"Verdict":"Skipped","Score":"0","Time":0,"Memory":0,"Message":""}]}]}'


GRADER API

Msg - Compiling
Msg - Judge test x
Group - Result { Score, Time, Mem, GroupResults} - For Each group
GroupResults = { Score, FullScore, Time, Status(Score, time, mem, verdict) }
Msg - Complete

Msg Compiling
Msg CompilationError
