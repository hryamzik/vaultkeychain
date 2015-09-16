#!/bin/bash

repo="$(git config --get remote.origin.url|sed -E 's/http(s)?:[/]{2}([^/]+)[/]/git@\2:/')"

test -n "$repo" || repo="$PWD"

if ! security find-generic-password -gw -s "$repo" -a "ansible-vault" -D "ansible vault"
then
    echo "Enter password for $repo:" 1>&2
    read pass
    security add-generic-password -a "ansible-vault" -s "$repo" -w "$pass" -D "ansible vault" -T ""
    echo $pass
fi
