#!/usr/bin/python
#
# ray@truedays.org May 09, 2016 v.01
#

import meetup.api

# My API KEY
KEYFILE = '/home/ray/github/sandbox/python/meetup/.meetup_api_key'; fopen = open(KEYFILE, "r"); KEY = str(fopen.readline().split()[0])
HOME='/home/ray/github/sandbox/python/meetup/'

client = meetup.api.Client(KEY)

GROUPS = ['Docker-Chicago', 'Docker-Dublin']

for GROUP in GROUPS:
  print "Pulling information on: ", GROUP
  group_info = client.GetGroup({'urlname': GROUP})
  dockers = []
  #FIXME this range should not be static
  for y in range(0,5):
    members_info = client.GetMembers({'group_id': group_info.id, 'offset': y})
    dockers = dockers + members_info.results
  print "Retrieved details on ", len(dockers), GROUP, "members."

  print "Saving to.. ", HOME+GROUP+'.out'; print
  fopen = open(HOME+GROUP+'.out', "a")
  for all in dockers:
    print all
    fopen.write(str(all))
  fopen.close()
print "Done"
