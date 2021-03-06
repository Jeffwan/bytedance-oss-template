# Copyright 2021 ByteDance and/or its affiliates.
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

from github import Github
import re

class ChangelogGenerator:
    def __init__(self, github_repo):
        # Replace <your_github_token> with your Github Token
        self._github = Github('<your_github_token>')
        self._github_repo = self._github.get_repo(github_repo)

    def generate(self, pr_id):
        pr = self._github_repo.get_pull(pr_id)

        return "{title} ([#{pr_id}]({pr_link}), @{user})".format(
            title=pr.title,
            pr_id=pr_id,
            pr_link=pr.html_url,
            user=pr.user.login
        )


# generated by `git log <oldTag>..HEAD --oneline`
payload = '''
6f1e96c4 Update container image for v1.1.1 (#1328)
e3061132 Remove vendor folder (#1288)
8d179f70 Fix: Remove Github CD workflow (#1263)
'''

g = ChangelogGenerator("you_org/your_repo")
for pr_match in re.finditer(r"#(\d+)", payload):
    pr_id = int(pr_match.group(1))
    print("* {}".format(g.generate(pr_id)))
