import os
import git
import shutil


def get_subfolders(directory):
    subfoldernames = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    subfolders = []
    for name in subfoldernames:
        subfolders.append(os.path.join(directory, name))
    return subfolders
    # subfolders = []
    # for root, dirs, files in os.walk(directory):
    #     for subfolder in dirs:
    #         subfolders.append(os.path.join(root, subfolder))
    # return subfolders


def get_git_repo_url(repo_path):
    """Returns the URL of the remote repository."""
    try:
        repo = git.Repo(repo_path)
        return repo.remotes.origin.url  # Get the remote URL
    except git.exc.InvalidGitRepositoryError:
        print(f"{repo_path} is not a valid Git repository.")
        return None


def re_clone_repository(repo_path):
    """Re-clones a repository."""
    # Get the URL of the repository
    repo_url = get_git_repo_url(repo_path)

    if not repo_url:
        print("Could not retrieve the repository URL. Exiting.")
        return
    else:
        print(f"Current git url : {repo_url}")

    # Get the parent directory of the repository
    parent_dir = os.path.dirname(repo_path)

    # Delete the existing repository folder
    print(f"Deleting the repository at {repo_path}")
    shutil.rmtree(repo_path)

    # Clone the repository back into the parent directory
    print(f"Cloning repository from {repo_url} into {parent_dir}")
    git.Repo.clone_from(repo_url, repo_path)


if __name__ == "__main__":
    directory = "E:/LibraryCode/ControlExample/"
    subfolders = get_subfolders(directory)
    print(subfolders)
    for repo_path in subfolders:
        re_clone_repository(repo_path)
