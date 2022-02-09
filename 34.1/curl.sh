curl --location --request POST 'http://localhost:3000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "Vinicius Gouveia"
}'

curl --location --request GET 'https://google.com/' \
--header 'Content-Type: application/json' \ -L 
