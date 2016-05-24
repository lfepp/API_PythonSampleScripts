#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# TODO add endpoint to v2 documentation
# NOTE Paul posted about this in #api https://pagerduty.slack.com/archives/api/p1464100853000048

import requests
import json

# Update to match your API key
API_KEY = '3c3gRvzx7uGfMYEnWKvF'

# Update to match the user ID of the user whose log entries you want to GET
USER_ID = 'P9GJP78'

# Update to match your chosen parameters
TIME_ZONE = 'UTC'
SINCE = ''
UNTIL = ''
IS_OVERVIEW = False
INCLUDE = []

def list_user_log_entries():
    url = 'https://api.pagerduty.com/users/' + USER_ID + '/log_entries'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY
    }
    payload = {
        'time_zone': TIME_ZONE,
        'is_overview': IS_OVERVIEW,
        'include': INCLUDE
    }
    if SINCE != '':
        payload['since'] = SINCE
    if UNTIL != '':
        payload['until'] = UNTIL
    r = requests.get(url, headers=headers, params=json.dumps(payload))
    print 'Status Code: ' + str(r.status_code)
    print r.json()

if __name__ == '__main__':
    list_user_log_entries()
