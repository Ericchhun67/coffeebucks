# CoffeeBucks Notes

## Fixed Header Spacing

When a navbar/header uses `position: fixed`, it floats on top of the page instead of taking up normal space.

That means page content can slide underneath it unless the page reserves space.

Fix:

```css
body {
    margin: 0;
    padding-top: 58px;
}
```

`padding-top` should roughly match the height of the fixed header.

## Margin vs Top

Use `margin-top` when you want normal space between sections.

Avoid using this for basic section spacing:

```css
position: relative;
top: 50px;
```

That visually moves the element, but it does not create normal layout space the same way margin does.

Better:

```css
.special-offers {
    margin-top: 80px;
}
```

## Fixed Elements Can Cover Content

`position: fixed` removes an element from the normal page layout.

That means other content does not know the fixed element is there.

Example:

```css
.site-container {
    position: fixed;
    top: 0;
    width: 100%;
}
```

This keeps the navbar stuck to the top of the screen, but page content may appear behind it.

Fix by adding space to the page:

```css
body {
    padding-top: 58px;
}
```

Use this when:

- The navbar/header is fixed
- The first section starts underneath the navbar
- Content looks hidden behind the top bar

## Footer Overlap

Avoid using `position: fixed` on a footer unless you specifically want it to stay on screen at all times.

For most websites, the footer should stay in normal page flow:

```css
.footer-container {
    width: 100%;
    padding: 12px 0;
    margin-top: 80px;
}
```

Normal footer behavior:

- Content appears first
- Footer appears after the content
- Footer does not cover sections above it

## Horizontal Image Groups

If images stack vertically, check the HTML order.

This stacks because the second image comes after the first image's text:

```html
<img>
<span>Description</span>
<img>
<span>Description</span>
```

Better structure:

```html
<div class="special-offers-grid">
    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>

    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>
</div>
```

Then make the parent horizontal:

```css
.special-offers-grid {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
}
```

Main idea:

The parent controls the row.
Each child card keeps its own image and description together.

## Aligning Two Images Horizontally

When two images need to line up side by side, use a parent container with two equal columns.

HTML structure:

```html
<div class="special-offers-grid">
    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>

    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>
</div>
```

CSS:

```css
.special-offers-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    align-items: start;
}
```

Why this works:

- `display: grid` makes the parent control layout
- `repeat(2, minmax(0, 1fr))` creates two equal columns
- Each `.special-offer-card` keeps one image and its description together
- Giving both images the same `height` makes their bottoms align

Responsive version:

```css
@media (max-width: 1000px) {
    .special-offers-grid {
        grid-template-columns: 1fr;
    }
}
```

This keeps the images horizontal on desktop and stacks them on smaller screens.

## Putting A Project On GitHub

You do not have to move a project to Desktop before putting it on GitHub.

The CoffeeBucks project can stay in Google Drive as long as Terminal is inside the project folder.

### CoffeeBucks GitHub Timeline

This is the order we went through for putting CoffeeBucks on GitHub.

1. The project was already in Google Drive.

That is okay. A project does not need to be on Desktop to use GitHub.

Important idea:

```text
Git works from whatever folder your project is in.
```

2. Option 1 was to keep the project where it already was.

Instead of moving the whole project, open Terminal and go into the CoffeeBucks folder.

Example:

```bash
cd "Google Drive/My Drive/Website developer/coffeebucks"
```

3. We made sure Git was being used inside the project folder.

If this error appears:

```text
fatal: not a git repository (or any of the parent directories): .git
```

it means Terminal is not inside the Git project folder yet.

Fix:

```bash
cd "Google Drive/My Drive/Website developer/coffeebucks"
```

Then check:

```bash
git status
```

4. We created a `.gitignore`.

The goal of `.gitignore` is to prevent unnecessary or private files from being uploaded.

Examples:

```text
venv/
__pycache__/
.env
.DS_Store
instance/
```

5. We checked that the project was already a Git repo.

The project was already on branch `main`.

Good result:

```text
On branch main
nothing to commit, working tree clean
```

6. The first GitHub push failed because GitHub does not accept normal passwords anymore.

Error:

```text
Password authentication is not supported for Git operations.
```

Meaning:

```text
Do not use your normal GitHub password for git push.
```

Use SSH or a personal access token.

7. We chose SSH.

SSH lets your Mac connect to GitHub using an SSH key instead of typing your GitHub password.

8. We installed GitHub CLI because the `gh` command was needed.

Check if GitHub CLI exists:

```bash
gh --version
```

If `gh` works, GitHub CLI is installed.

9. We logged in with GitHub CLI.

Command:

```bash
gh auth login
```

Choices:

```text
GitHub.com
SSH
Upload or create SSH key
Login with a web browser
```

10. GitHub asked for an SSH key title.

That title is only a name for the key on GitHub.

Example:

```text
Eric MacBook Pro
```

11. GitHub gave a browser device code.

The code from Terminal gets typed into the GitHub browser page.

The browser page may say:

```text
Authorize your device
```

After entering the code, GitHub CLI can finish logging in.

12. We tested SSH.

Command:

```bash
ssh -T git@github.com
```

Good result:

```text
Hi Ericchhun67! You've successfully authenticated...
```

13. The SSH key had a passphrase problem.

If Terminal says:

```text
Enter passphrase for key
```

that means the SSH key has a password/passphrase.

If you forgot it, you cannot recover that passphrase.

The fix is to create a new SSH key.

14. We created a new SSH key with no passphrase.

Command:

```bash
ssh-keygen -t ed25519 -C "Ericchhun67 GitHub" -f ~/.ssh/id_ed25519
```

When it asks:

```text
Enter passphrase
```

press `Enter`.

When it asks again:

```text
Enter same passphrase again
```

press `Enter` again.

15. We uploaded the new public key to GitHub.

Command:

```bash
gh ssh-key add ~/.ssh/id_ed25519.pub --title "Eric MacBook Pro"
```

Good result:

```text
Public key added to your account
```

16. We tested SSH again.

Command:

```bash
ssh -T git@github.com
```

Good result:

```text
Hi Ericchhun67! You've successfully authenticated...
```

17. GitHub said the repository was not found.

Error:

```text
ERROR: Repository not found.
```

Meaning:

```text
The GitHub repo probably did not exist yet, or the remote URL was wrong.
```

18. We created the GitHub repository.

Command:

```bash
gh repo create coffeebucks --public --source=. --remote=origin --push
```

Good result:

```text
Created repository Ericchhun67/coffeebucks on github.com
```

19. GitHub also said it could not add `origin`.

Message:

```text
Unable to add remote "origin"
```

Meaning:

```text
The project already had a remote called origin.
```

That was not the main problem.

20. We checked/fixed the remote.

Command:

```bash
git remote set-url origin git@github.com:Ericchhun67/coffeebucks.git
```

Check it:

```bash
git remote -v
```

Correct result:

```text
origin  git@github.com:Ericchhun67/coffeebucks.git (fetch)
origin  git@github.com:Ericchhun67/coffeebucks.git (push)
```

21. We pushed the project to GitHub.

Command:

```bash
git push -u origin main
```

Good result:

```text
main -> main
branch 'main' set up to track 'origin/main'
```

That means CoffeeBucks is on GitHub.

22. After the first push, the workflow is shorter.

Use:

```bash
git status
git add .
git commit -m "Describe what changed"
git push
```

No need to log in every time.

No need to use `-u origin main` every time.

### 1. Go To The Project Folder

Git commands must be run inside the folder that contains the project.

Example:

```bash
cd "Google Drive/My Drive/Website developer/coffeebucks"
```

Check that you are in the right place:

```bash
pwd
ls
```

You should see project files like:

```text
app.py
static
templates
routes
models
```

### 2. Create A `.gitignore`

`.gitignore` tells Git what not to upload.

Useful Flask/Python `.gitignore`:

```text
__pycache__/
*.pyc
venv/
.venv/
.env
.flaskenv
instance/
.DS_Store
.vscode/
.idea/
```

Do not upload secret files like `.env`.

### 3. Start Git In The Project

Only do this once per project:

```bash
git init
```

Check the status:

```bash
git status
```

### 4. Add And Commit The Project

Stage the files:

```bash
git add .
```

Commit the files:

```bash
git commit -m "Initial CoffeeBucks project"
```

Check again:

```bash
git status
```

Good result:

```text
nothing to commit, working tree clean
```

### 5. Install GitHub CLI If Needed

GitHub CLI is the `gh` command.

Check if it exists:

```bash
gh --version
```

If Terminal says `command not found`, GitHub CLI needs to be installed.

### 6. Log In To GitHub CLI

Run:

```bash
gh auth login
```

Choices used:

```text
GitHub.com
SSH
Generate or upload an SSH key
Login with a web browser
```

If it asks for a title for the SSH key, the title is just a name that GitHub shows.

Example:

```text
Eric MacBook Pro
```

If it gives a browser code, copy the code into the GitHub browser page.

Good result:

```text
You have successfully authenticated
```

### 7. Test SSH

Run:

```bash
ssh -T git@github.com
```

Good result:

```text
Hi Ericchhun67! You've successfully authenticated...
```

This means GitHub trusts the Mac's SSH key.

### 8. Create The GitHub Repository

From inside the project folder:

```bash
gh repo create coffeebucks --public --source=. --remote=origin --push
```

Private version:

```bash
gh repo create coffeebucks --private --source=. --remote=origin --push
```

If it says:

```text
Created repository Ericchhun67/coffeebucks on github.com
```

the GitHub repo was created.

If it also says:

```text
Unable to add remote "origin"
```

that usually means the project already has a remote named `origin`.

That is not always a problem.

### 9. Check The Remote

Run:

```bash
git remote -v
```

The CoffeeBucks remote should look like:

```text
origin  git@github.com:Ericchhun67/coffeebucks.git (fetch)
origin  git@github.com:Ericchhun67/coffeebucks.git (push)
```

If the remote is wrong, fix it with:

```bash
git remote set-url origin git@github.com:Ericchhun67/coffeebucks.git
```

### 10. First Push

First push:

```bash
git push -u origin main
```

`-u origin main` connects the local `main` branch to the GitHub `main` branch.

Good result:

```text
main -> main
branch 'main' set up to track 'origin/main'
```

That means the project is now on GitHub.

CoffeeBucks GitHub page:

```text
https://github.com/Ericchhun67/coffeebucks
```

### 11. Normal Workflow After The First Push

After the first push, use this workflow:

```bash
git status
git add .
git commit -m "Describe what changed"
git push
```

You usually do not need `git push -u origin main` again.

After tracking is set up, `git push` is enough.

### Common GitHub Errors

```text
Permission denied (publickey)
```

GitHub does not recognize the SSH key being used.

Try:

```bash
ssh -T git@github.com
```

```text
Repository not found
```

The GitHub repo does not exist yet, the repo name is wrong, or the remote URL has a typo.

```text
Password authentication is not supported
```

GitHub does not let you push with your normal GitHub password anymore.

Use SSH or a personal access token instead.

```text
Unable to add remote "origin"
```

The project already has a remote named `origin`.

Check it with:

```bash
git remote -v
```

### Important Reminder

Closing Terminal usually does not log you out of GitHub.

If GitHub CLI and SSH are already set up, the next push should just be:

```bash
git push
```
