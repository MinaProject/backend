from elasticgit import EG
from elasticinit import TestStory
import json


def push_to_git(repo_path, index_prefix, es_host):
    workspace = EG.workspace('repos/test_content',
                             index_prefix=index_prefix,
                             es={'urls': [es_host]})
    if workspace.repo.remotes:
        repo = workspace.repo
        remote = repo.remote()
        remote.fetch()
        remote_master = remote.refs.master
        remote.push(remote_master.remote_head)


def pull_from_git(repo_path, index_prefix, es_host):
    workspace = EG.workspace(repo_path,
                             index_prefix=index_prefix,
                             es={'urls': [es_host]})
    # replace bottoms stuff with worksapce.pull
    if workspace.repo.remotes:
        repo = workspace.repo
        remote = repo.remote()
        remote.fetch()
    storyList = workspace.S(TestStory)
    return json.dumps([dict(a.to_object()) for a in storyList])


def setup_workspace(repo_path, index_prefix, es_host):
    workspace = EG.workspace(repo_path,
                             index_prefix=index_prefix,
                             es={'urls': [es_host]})
    workspace.setup('foo', 'minaglobalfoundation@gmail.com')
    while not workspace.index_ready():
        pass
    return workspace
