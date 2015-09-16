# vaultkeychain
Scripts to link ansible-vault and keychain

## Usage
### MAC OS

```bash
git clone https://github.com/gitinsky/vaultkeychain.git
ln -vs "$PWD/vaultkeychain/vaultkeychain.sh" ~/sbin/vaultkeychain
```

Your ansible.cfg:

```ini
[defaults]
vault_password_file = ~/sbin/vaultkeychain
```
