import subprocess

def delete_branches_except_default(repo_path, default_branch):
    # Navigate to the repository and checkout the default branch
    subprocess.run(['git', 'checkout', default_branch], cwd=repo_path)

    # Get all remote branches
    result = subprocess.run(['git', 'branch', '-r'], cwd=repo_path, stdout=subprocess.PIPE, text=True)
    branches = result.stdout.splitlines()

    # Filter out the default branch and create a list of branches to delete
    branches_to_delete = [branch.strip() for branch in branches if branch.strip() != f'origin/{default_branch}']

    # Delete each branch using the full remote reference format
    for branch in branches_to_delete:
        branch_name = branch.strip()  # Keep the full remote reference
        print(f'Deleting branch: {branch_name}')
        subprocess.run(['git', 'push', 'origin', '--delete', branch_name], cwd=repo_path)

def delete_tags(repo_path):
    # Get all remote tags
    result = subprocess.run(['git', 'tag', '-l'], cwd=repo_path, stdout=subprocess.PIPE, text=True)
    tags = result.stdout.splitlines()

    # Delete each tag
    for tag in tags:
        tag_name = tag.strip()
        print(f'Deleting tag: {tag_name}')
        subprocess.run(['git', 'push', 'origin', '--delete', tag_name], cwd=repo_path)

if __name__ == '__main__':
    repo_path = 'path/to/your/local/platform_frameworks_base'  # Update this path
    default_branch = '15'
    delete_branches_except_default(repo_path, default_branch)
    delete_tags(repo_path)
