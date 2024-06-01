import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('revolmax')
    assert user['login'] == 'revolmax'

@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('non_existing_user')
    #print(r)
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    print(r)  
    assert r['total_count'] == 57  
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_can_not_be_found(github_api):
    r = github_api.search_repo('revolmax_non_existing_repo')
    print(r)  
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0  
    