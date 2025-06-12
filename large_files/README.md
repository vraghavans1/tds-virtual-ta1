This directory contains placeholders for large files that exceed the 4MB size limit of the Codex environment. For example, the "80 MB" `knowledge_base.db` cannot be uploaded directly.

GitHub's web interface only allows files up to 25 MB. To include bigger files, you must use Git LFS (Large File Storage).

Steps to add `knowledge_base.db` using Git LFS:
1. Install Git LFS if you haven't already: `git lfs install`
2. Track the file path: `git lfs track "knowledge_base.db"`
3. Add the file and `.gitattributes`: `git add .gitattributes knowledge_base.db`
4. Commit and push as usual.

After pushing, the real file will be stored using Git LFS, while your repository only contains a small pointer file.
