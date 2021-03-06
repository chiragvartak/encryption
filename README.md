# Using GPG in Your Regular Workflow

There is nothing special with the code in this repository. This Python code just calls the GnuPG `gpg` command with the proper parameters. This code is more intended to put some habits into you so that your files remain always secure and you never leave them unsafe because you "forgot to remove that temporary encrypted file".

Make an alias in your `.bash_aliases` or wherever you do that on Windows:

```bash
alias secret="python /path/to/encryption.py"
```

Then it's usage is as follows.

## Creating a New File or Encrypting an Existing File

To create a new file (which will be encrypted after you put content into it), or, to encrypt an existing file:

```bash
secret <filename>
```

Note that the above `filename` should NOT be a `.gpg` file.

## Editing or Viewing a File in Editor

Just do this:

```bash
secret <filename>.gpg
```

The file you specify should be an encrypted file (of course!). It should end with a `.gpg` extension.

## Some Rules to Follow

1. Always encrypt and view your files using the `secret` command. Do not directly use `gpg`.

2. That's it. That's the only rule you should follow to keep your files always secure.

## Some Things to Note

1. I am assuming that you have `gpg` installed and that it is available through the `PATH`.

2. Also assuming that Sublime Text is installed and that it is available through the `PATH` with the `subl` command. With some minor modifications you should be able to use any other editor. Just make sure that it is accessible through `PATH` and that it holds the terminal when run. Actually this is the reason I am using `subl -w` rather than simply `subl`.

3. Yet another assumption: I hope you have set the private-public key pairs in your GnuPG.

4. Never do `Ctrl+C`. I haven't considered what happens when you interrupt the program.
