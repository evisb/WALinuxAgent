# Windows Azure Linux Agent
#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

from azurelinuxagent.metadata import DistroName, DistroVersion, DistroFullName

def GetOSUtil():
    from osutil import SUSE11OSUtil, SUSEOSUtil
    if DistroFullName=='SUSE Linux Enterprise Server' and DistroVersion < '12' \
            or DistroFullName == 'openSUSE' and DistroVersion < '13.2':
        return SUSE11OSUtil()
    else:
        return SUSEOSUtil()
