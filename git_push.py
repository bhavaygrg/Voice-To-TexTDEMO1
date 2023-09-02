from github import Github

# Your GitHub personal access token
github_token = 'Your token'

# GitHub repository information
repo_owner = 'bhavaygrg'
repo_name = 'githubpushtrials'

# Local path to the Markdown file you want to push
file_path = 'output.md'

# Initialize a GitHub instance with your token
g = Github(github_token)

# Get the repository
repo = g.get_repo(f'{repo_owner}/{repo_name}')

# Read the content of the local file
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Create a new file in the repository
repo.create_file(
    path='output.md',  # Remote file path
    message='Add output.md',  # Commit message
    content=file_content,  # File content as base64-encoded string
    branch='main'  # Branch where you want to create the file
)

print(f'File "{file_path}" has been pushed to the "{repo_owner}/{repo_name}" repository.')
