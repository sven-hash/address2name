# address2name

This repo store the mapping between address and name for [Alephium](alephium.org)


It is used in:

- [https://t.me/alephiumgroup](https://t.me/alephiumgroup)
- [https://twitter.com/AlephiumWW](https://twitter.com/AlephiumWW)

## Add a mapping

To add a mapping request you should do a PR with some information, to be sure this is you, you have to sign the data:

`Name: {the name you want} address: {your wallet address}` (this should be converted in hexadecimal [converter](https://www.rapidtables.com/convert/number/ascii-to-hex.html)


## Data format for pull request

Format in the file: `address;timestamp;name`

To get the timestamp you could use [timestamp.online](https://timestamp.online/)


### How to sign

#### Using swagger

1. Go to [http://127.0.0.1:12973/docs](http://127.0.0.1:12973/docs) under `Wallets`
2. Open the entry `/wallets/{wallet_name}/sign` (unlock your wallet first)
3. Write your wallet name and replace the `"data":"{your data}"` with your data you want to sign (in [hexadecimal](https://www.rapidtables.com/convert/number/ascii-to-hex.html)). Then execute
4. Scroll down, you should see an entry with `"signature":"..."`. Copy the signature and add it to the PR

#### Using curl

1. `curl -X 'POST' \
  'http://127.0.0.1:12973/wallets/{wallet-name}/sign' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": "{your data}"
}'`

2. Copy the signature and add it to the PR
 
