# Dungeons and Dragons bot
Telegram bot for the game "Dungeons and Dragons"

## Contributing

### 1. Create fork
Create a fork of the main repository, this will create a copy of the main repository on your account, and you will be able to upload your changes to it and create pull requests.
([How to create fork](https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo))

### 2. Download
Download the repository from your fork to your computer so that you can add your changes to it.
Replace <your_username> with your user's name
```Bash
git clone https://github.com/<your_username>/Dungeons_and_Dragons_bot.git
```

### 3. Go to the working folder
```Bash
cd ./Dungeons_and_Dragons_bot/
```

### 4. Create new branch
Replace <your_patches> with the name of the branch you will be making your changes to.
```Bash
git checkout -b <your_patches>
```

### 5. Make your changes
Add new features, improve existing ones, fix the wrong ones, in a word, contribute.

### 6. Save the changes
```Bash
git add .
```
Add a short description of what you have changed in single quotes.
Also, your message must comply with [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
```Bash
git commit -m ''
```

### 7. Switch to the main branch
```Bash
git checkout main
```

### 8. Upload changes from the main repository
The first command should be used only once, it creates a downstream, using which you will download changes from the original repository.
If you have already executed the first command, then skip it this time and all subsequent times, execute only the second command.
```Bash
git remote add downstream https://github.com/SynKolbasyn/Dungeons_and_Dragons_bot.git
```
```Bash
git pull downstream main
```

### 9. Merge your branch from the main one and fix conflicts if they appear
Replace <your_patches> with the name of the branch you will be making your changes to.
```Bash
git merge <your_patches>
```

### 10. Upload the changes to the remote repository
```Bash
git push origin main
```

### 11. Create a pull request, add a title, description, and wait for a response from the maintainer
[How to create pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

### 12. Support
If suddenly something doesn't work out for you, feel free to email me, I will try to help.
```
syn.kolbasyn.06@gmail.com
```

## Roadmap
1. Add documentation
2. [A detailed README description](https://opensource.guide/starting-a-project/#writing-a-readme)
3. [A code of conduct](https://opensource.guide/starting-a-project/#establishing-a-code-of-conduct)
4. [Contributing guidelines](https://opensource.guide/starting-a-project/#writing-your-contributing-guidelines)
5. Add a translation.
6. Add mechanics of moving between locations.
7. Add character creation mechanics.
8. Add combat mechanics
9. Add item mechanics
10. Add illustrations

## Tests
Before doing this, you should set the PROJECT_DIR system variable, which will store the path to the folder of this project
```Bash
python -m pytest
```
uwu 
