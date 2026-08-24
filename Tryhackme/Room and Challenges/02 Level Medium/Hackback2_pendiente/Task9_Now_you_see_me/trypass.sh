#!/bin/bash
cd /mnt/c/Users/pente/Downloads/reversing_THM/stego1 || exit 1
for p in 5f4dcc3b5aa765d61d8327deb882cf99 alan grace password123 12345678 thm qwerty turing alan2 grace123 harvard marki 123456789 p4ssw0rd; do
  out=$(gpg --batch --yes --passphrase "$p" -o /tmp/o.bin -d flag2.mp3 2>&1)
  if ! echo "$out" | grep -q "Bad session key"; then
    echo "PASS=[$p] -> $out"
  fi
done
echo "=== done ==="
