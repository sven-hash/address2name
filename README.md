# address2name

Store the mapping between address and name for [Alephium](alephium.org)

Used in:

- [https://t.me/alephiumgroup](https://t.me/alephiumgroup)
- [https://twitter.com/AlephiumWW](https://twitter.com/AlephiumWW)

## How to claim

To add a mapping request you should modify the file `known-wallets.txt`:

- If your address already exists modify the associated name and replace `identified` or `guessed` by `verified` 
- If youe address doesn't exists in the file add `<your wallet address>;< the name you want>;verified` 

**And create a merge request with the following information:**

In the MR you have to add:

- Title: name you want (limited to 12 characters, will be replace by "..." if longer)
- Content

```
Validation data:
{
  "data": "<data>",
  "signature": "<signature>",
  "publicKey": "<your public key>"
}
```

Note: The signature obtained by signing the data `<your wallet address>;< the name you want>` (this should be converted in hexadecimal [converter](https://www.rapidtables.com/convert/number/ascii-to-hex.html))


### How to get the public key

#### Using swagger

1. Go to [http://127.0.0.1:12973/docs](http://127.0.0.1:12973/docs) under `Wallets`
2. Open the entry `/wallets​/{wallet_name}​/addresses​/{address}` (unlock your wallet first)
3. Write your wallet name and the address you want. Then execute
4. Scroll down, you should see an entry with `"publickey":"..."`. Copy the signature and add it to the PR

#### Using curl

1. `curl -X 'http://127.0.0.1:12973/​wallets​/{wallet_name}​/addresses​/{address}' -H 'accept: application/json' -H 'Content-Type: application/json' `
2. Copy the public and add it to the PR

### How to sign

#### Using swagger

1. Go to [http://127.0.0.1:12973/docs](http://127.0.0.1:12973/docs) under `Wallets`
2. Open the entry `/wallets/{wallet_name}/sign` (unlock your wallet first)
3. Write your wallet name and replace the `"data":"{your data}"` with your data you want to sign (in [hexadecimal](https://www.rapidtables.com/convert/number/ascii-to-hex.html)). Then execute
4. Scroll down, you should see an entry with `"signature":"..."`. Copy the signature and add it to the PR

#### Using curl

1. ` curl -X 'POST' 
  'http://127.0.0.1:12973/wallets/{wallet-name}/sign' 
  -H 'accept: application/json' 
  -H 'Content-Type: application/json' 
  -d '{
  "data": "{your data}"
}' `

2. Copy the signature and add it to the PR
