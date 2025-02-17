import os
import git

def generate_commit_message(diff_text):
    if not diff_text.strip():
        return "Latest commit"
    return f"Updated code with changes: {len(diff_text.splitlines())} lines affected."

def main(repo_path):
    if not os.path.exists(repo_path):
        print(f"Repository path '{repo_path}' does not exist.")
        return

    try:
        # Open the repository
        repo = git.Repo(repo_path)

        # Get the latest commit
        latest_commit = repo.head.commit

        # Check if the latest commit has any parents
        if latest_commit.parents:
            diffs = latest_commit.diff(latest_commit.parents[0])
        else:
            print("No parent commit found. This may be the first commit.")
            return

        # Collect the diff information
        diff_text = "".join(diff.diff for diff in diffs)
        # Generate commit message
        commit_message = generate_commit_message(diff_text)

        # Print the generated commit message
        print("Generated Commit Message:")
        print(commit_message)

        repo.git.add(A=True)
        repo.index.commit(commit_message)

        origin = repo.remote(name='origin')
        origin.push()
        print("Changes pushed to the remote repository.")
    except git.exc.InvalidGitRepositoryError:
        print(f"Directory '{repo_path}' is not a valid git repository.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    repository_path = r'C:\Users\KIIT\OneDrive\Desktop\Workik\Git Commit'  # Ensure this is correct
    main(repository_path)