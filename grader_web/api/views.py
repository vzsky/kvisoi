from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.models import Submission, GroupResult, CaseResult

@csrf_exempt
def apistatus (req) :
  return JsonResponse("api is on", safe=False)

@csrf_exempt
def message (req) :
  if req.method == 'POST' : 
    data = json.loads(req.body)
    sid = data['SubmissionID']
    msg = data['Message']
    try :
      submission = Submission.objects.get(id=sid)
      submission.status = msg
      submission.save()
    except :
      raise
    return JsonResponse("Success", safe=False)
  return JsonResponse("post only (msg)", safe=False)

@csrf_exempt
def group (req) :
  if req.method == 'POST' : 
    data = json.loads(req.body)
    sid = data['SubmissionID']
    result = data['Results']
    try :
      submission = Submission.objects.get(id=sid)
      index = len(submission.groupresult_set.all())
      print(result)
      submission.score = result['Score']
      submission.timeUsed = result['Time']
      submission.memoryUsed = result['Memory']
      submission.save()
      newGroupData = result['GroupResults'][index]

      newGroup = GroupResult(
        submission=submission,
        score=newGroupData['Score'],
        fullScore=newGroupData['FullScore'],
      )
      newGroup.save()
      for num, case in enumerate(newGroupData['Status']) :
        newcase = CaseResult(
          id=num+1,
          group=newGroup,
          verdict=case['Verdict'],
          score=case['Score'],
          timeUsed=case['Time'],
          memoryUsed=case['Memory'],
          message=case['Message']
        )
        newcase.save()
    except :
      raise
    return JsonResponse("Success", safe=False)
  return JsonResponse("post only (group)", safe=False)