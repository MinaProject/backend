from elasticgit import EG
from elasticinit import TestStory
import json


def push_to_git(repo_path, index_prefix, es_host):
    workspace = EG.workspace(repo_path,
                             index_prefix=None,
                             es={'urls': [es_host]})
    if workspace.repo.remotes:
        repo = workspace.repo
        remote = repo.remote()
        remote.fetch()
        remote_master = remote.refs.master
        remote.push(remote_master.remote_head)


def pull_from_git(repo_path, index_prefix, es_host):
    workspace = EG.workspace(repo_path,
                             index_prefix=None,
                             es={'urls': [es_host]})
    # workspace.sync(TestStory)
    workspace.pull()
    storyList = workspace.S(TestStory)
    return json.dumps([dict(a.to_object()) for a in storyList])


def delete_from_git(storyUUID):
    workspace = EG.workspace('repos/test_content',
                             index_prefix=None,
                             es={'urls': ['http://localhost:9200']})
    workspace.setup('Codie Roelf', 'codiebeulaine@gmail.com')

    stories = workspace.S(TestStory)
    for story in stories:
        if story.uuid == storyUUID:
            workspace.delete(story.get_object(), 'deleting')
            print('deleted')
    if workspace.repo.remotes:
        repo = workspace.repo
        remote = repo.remote()
        remote.fetch()
        remote_master = remote.refs.master
        remote.push(remote_master.remote_head)
    workspace.refresh_index()


def setup_workspace(repo_path, index_prefix, es_host):
    workspace = EG.workspace(repo_path,
                             index_prefix=index_prefix,
                             es={'urls': [es_host]})
    workspace.setup('foo', 'minaglobalfoundation@gmail.com')
    while not workspace.index_ready():
        pass
    return workspace
