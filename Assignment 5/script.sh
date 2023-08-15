for i in $(cat < "inputs.txt")
do
curl -H "Content-Type: application/json" --request POST --data '{"teamname":"hardwired","password":"hardwired", "plaintext":"'"$i"'"}' -k https://172.27.26.188/eaeae >> outputs.txt
done