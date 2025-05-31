# del_github

⚠️ **Warning:** This script will **permanently delete all your GitHub repositories** under the authenticated account. Use with extreme caution and at your own risk.

## Overview

`del_github` is a simple Python utility that uses the GitHub API to delete **all repositories** associated with a user account. It can be useful for cleaning up test accounts, resetting demo environments, or managing temporary repositories.

## Features

- Deletes all repositories owned by the authenticated GitHub user
- Uses GitHub's official REST API
- Easy setup with `.env` file
- Clear console output for success/failure of each deletion

## Requirements

- Python 3.6+
- GitHub Personal Access Token with `repo` scope (for private repo deletion)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tameronline/del_github.git
   cd del_github
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following content:

   ```
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_github_token
   ```

   > 💡 You can create a personal access token at: [https://github.com/settings/tokens](https://github.com/settings/tokens)

## Usage

Run the script using:

```bash
python myapp.py
```

Each repository deletion will be printed to the console with either:

- ✅ `Successfully deleted: repo_name`
- ❌ `Failed to delete: repo_name – Status code: xxx`

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

## Disclaimer

This script performs **irreversible deletions**. Ensure you have backups or that the repositories are no longer needed before running. The author assumes **no responsibility** for accidental data loss.
