#!/usr/bin/env python3

# Fetches an archive with markdown using Notion API
#
# Expects a Notion token in the `NOTION_TOKEN` environment variable.
# Get this token from your browser’s cookies.
#
# Usage: NOTION_TOKEN=<token> ./notion.py <page-url>
#

import json
import os
import re
import requests
import sys
from time import sleep

def url_to_block_id(page_url):
  m = re.match(r'^https://www.notion.so/[^/]+/[^/]+-([0-9A-Fa-f]+)$', page_url)
  if not m or not m.group(1):
      raise ValueError('Illegal notion URL: {}'.format(page_url))
  s = m.group(1)
  chunks = [ s[4*i:4*i+4] for i in range(0, len(s)//4) ]
  return '{}{}-{}-{}-{}-{}{}{}'.format(*chunks)

def get_block_id(page_id):
  return r.json()['recordMap']['block'].keys()[0]

def get_task_status(task_id, cookies):
  payload = {
    'taskIds': [task_id],
  }
  r = requests.post(
    'https://www.notion.so/api/v3/getTasks',
    cookies=cookies,
    json=payload,
  )
  result = r.json()['results'][0]
  print(result)
  return (result['state'], result.get('status', None))

def wait_for_task(task_id, cookies):
  for i in range(5):
    (state, status) = get_task_status(task_id, cookies)
    if state in ['not_started', 'in_progress']:
      sleep(1)
    elif state == 'success':
      return status
    else:
      raise Exception('Unexpected task state: {}'.format(state))
  else:
    raise Exception('Tired of waiting for the export task')

def get_exported_url(block_id, cookies):
  payload = {
    'task': {
      'eventName': 'exportBlock',
      'request': {
        'blockId': block_id,
        'exportOptions': {
          'exportType':'markdown',
          'timeZone': 'UTC',
          'locale':'en'
        },
        'recursive': False
      },
    },
  }
  r = requests.post(
    'https://www.notion.so/api/v3/enqueueTask',
    cookies=cookies,
    json=payload,
  )
  task_id = r.json().get('taskId', None)
  if not task_id:
    raise Exception('Could not get the scheduled task id: {}'.format(r))

  result = wait_for_task(task_id, cookies)
  url = result.get('exportURL', None)
  if not url:
    raise Exception('Unexpected task result: {}'.format(result))
  return url



