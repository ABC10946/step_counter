import subprocess

repos = open('repo_list.txt').read().split()
username = open('user.txt').read().strip()
max_count = len(repos)
num = 0

for repo in repos:
    num += 1
    print(num, '/', max_count, ':', repo)
    subprocess.getoutput('git clone git@github.com:{}/{} temp_linecount_repo'.format(username, repo))
    output = subprocess.getoutput('cloc temp_linecount_repo --report-file=./reports/{}_{}_report'.format(username, repo))
    subprocess.getoutput('rm -rf temp_linecount_repo')

repos_reports = ['./reports/' + username + '_' + repo + '_report' for repo in repos]

print(subprocess.getoutput('cloc --sum-reports {}'.format(' '.join(repos_reports))))
