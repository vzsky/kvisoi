from grader_web.settings import supportedLangs

def supportedlangs (req) :
  lang2codemirror = {}
  for lang in supportedLangs :
    lang2codemirror[lang] = supportedLangs[lang]["codemirror"]
  print(lang2codemirror)
  return {
    "lang2codemirror" : lang2codemirror
  }