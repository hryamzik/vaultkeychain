# vaultkeychain
Scripts to link ansible-vault and keychain. Keychain username is set to a git remote URL in git@ format if it could be determined, otherwize current system path is used instead.

## Installation
### MAC OS

```bash
git clone https://github.com/gitinsky/vaultkeychain.git
ln -vs "$PWD/vaultkeychain/vaultkeychain.py" ~/sbin/vaultkeychain
```

Or for shell version:

```bash
ln -vs "$PWD/vaultkeychain/vaultkeychain.sh" ~/sbin/vaultkeychain
```

## Usage

#### ansible.cfg:

```ini
[defaults]
vault_password_file = ~/sbin/vaultkeychain
```

## Test

Run

```bash
PAGER=cat ansible-vault view vaulted.yml
```

Password is ```vaultkeychain```.

On the second run password should be retreived from your keychain.

#### env

```bash
export ANSIBLE_VAULT_PASSWORD_FILE=~/sbin/vaultkeychain
```

# Other resources
[ansible-tools](https://github.com/lvillani/ansible-tools)
