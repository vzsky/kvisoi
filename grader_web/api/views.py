from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.models import Submission, GroupResult, CaseResult
import logging
logger = logging.getLogger("mylogger")

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
    logger.info("POST TO GROUP")
    data = json.loads(req.body)
    sid = data['SubmissionID']
    result = data['Results']
    try :
      submission = Submission.objects.get(id=sid)
      logger.info(f'group message of submission {sid}')
      submission.score = result['Score']
      submission.timeUsed = result['Time']
      submission.memoryUsed = result['Memory']
      submission.save()
      logger.info('submission updated')

      index = len(submission.groupresult_set.all())
      # should change to a for from index to result['GroupResults'].size()
      newGroupData = result['GroupResults'][index]

      newGroup = GroupResult(
        submission=submission,
        score=newGroupData['Score'],
        fullScore=newGroupData['FullScore'],
      )
      newGroup.save()
      logger.info(f"group # {len(submission.groupresult_set.all())} saved successfully")
      for case in newGroupData['Status'] :
        newcase = CaseResult(
          group=newGroup,
          verdict=case['Verdict'],
          score=case['Score'],
          timeUsed=case['Time'],
          memoryUsed=case['Memory'],
          message=case['Message']
        )
        newcase.save()
      logger.info(f"all cases saved, cases : {newGroup}")
      logger.info(f"submission {sid} response is set to {submission.response}")
    except :
      raise
    return JsonResponse("Success", safe=False)
  return JsonResponse("post only (group)", safe=False)