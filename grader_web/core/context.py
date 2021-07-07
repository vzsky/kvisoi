from grader_web.settings import supportedLangs
import json

def supportedlangs (req) :
  lang2codemirror = {}
  for lang in supportedLangs :
    lang2codemirror[lang] = supportedLangs[lang]["codemirror"]
  return {
    "lang2codemirror" : lang2codemirror,
    "json_lang2codemirror" : json.dumps(lang2codemirror),
  }