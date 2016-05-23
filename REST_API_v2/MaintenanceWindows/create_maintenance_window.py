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

import requests
import json

# Update to match your API key
API_KEY = '3c3gRvzx7uGfMYEnWKvF'

# Update to match your email address
EMAIL = 'lucas@pagerduty.com'

# Update to match your chosen parameters
START_TIME = '2016-05-23T14:00:00-07:00'
END_TIME = '2016-05-23T18:00:00-07:00'
DESCRIPTION = 'Enter your maintenance window description here'
SERVICES = [{
    'id': 'PKWA90D',
    'type': 'service_reference'
}]
TEAMS = []
TYPE = 'maintenance_window'

def create_maintenance_window():
    url = 'https://api.pagerduty.com/maintenance_windows'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY,
        'Content-type': 'application/json',
        'From': EMAIL
    }
    payload = {
        'maintenance_window': {
            'start_time': START_TIME,
            'end_time': END_TIME,
            'description': DESCRIPTION,
            'services': SERVICES,
            'teams': TEAMS,
            'type': TYPE
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print 'Status Code: ' + str(r.status_code)
    print r.json()

if __name__ == '__main__':
    create_maintenance_window()
