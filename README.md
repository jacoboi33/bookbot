# bookbot
BookBot is my first git project from boot.dev!

# Install pyenv with webi
### Run this command to install pyenv with webi.
    curl -sS https://webi.sh/pyenv | sh

By the way, give the Webi repo a star on GitHub if you like it!

Make sure to read the installation logs! They are probably telling you to do the following:

Open your ~/.bashrc (or ~/.zshrc on Mac) file in VS Code. You can do so by typing:
    code ~/.bashrc

Add these lines to the bottom of the file:

    export PYENV_ROOT="$HOME/.pyenv"
    command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

INSTALL PYTHON 3
Now that you have pyenv, run this command to install Python 3.12.1:

    pyenv install -v 3.12.1
Then set that version as your default:

    pyenv global 3.12.1
Finally, make sure that it worked:

    python --version
You should get back the correct Python version!

DEBUG NOTE
If the above command is not working you may need to call it using python3 instead:

    python3 --version