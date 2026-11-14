"""
RECORD CHECK  -  my version
===========================

Name  : Imani Slater
Lane  : Cyber
Date  : Thursday 12th Nov

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
  """ cleans and breaks(parse) one record """
  cleaned = raw_line.strip()
  record = {}

  for piece in cleaned.split(","):
    key, value = piece.split("=", 1)
    key = key.strip().lower()
    value = value.strip()

    if key == "attempts":
      value = int(value)
    elif key == "result":
      value = value.upper()

    record[key] = value

  return record

def status_of(record):
  """ returns flagged for failed attempts and ok for other returns"""
  if record["result"] == "FAILED":
    return "FLAGGED"
  else:
    return "OK"

raw_records = [
    " SRC=10.0.0.5, ATTEMPTS=12, RESULT=FAILED ",
    "src=10.0.0.8,attempts=2,result=success",
    " SRC = 192.168.1.10 , ATTEMPTS = 7 , RESULT = Failed ",
    "src=172.16.0.4, attempts=0, result=SUCCESS",
    "Src=10.0.0.20, Attempts=15, Result=failed"
]

for raw_record in raw_records:
    record = parse_line(raw_record)

    print(record)
    print(status_of(record))
    print()
    
