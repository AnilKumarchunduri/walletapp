WalletApp prerequisites :

python >= 3.8, npm 14.x
##3rd-party dependencies are mentioned in requirement.txt.

##After installing the above packages you can run below commands :

##To Start the App in the docker run the below command :
```
git clone https://github.com/AnilKumarchunduri/walletapp.git
cd walletapp/
docker build -t walletapp:prd -f Dockerfile .
docker run -dt -p <hostport>:8012 --name walletapp walletapp:prd
example :
    docker run -dt -p 8000:8012 --name walletapp walletapp:prd
    open the link in your browser http://<hostname>:8000/wallet/
```

##To start the app in your local run the below commands
```
git clone https://github.com/AnilKumarchunduri/walletapp.git
cd walletapp/
```
##Install the requried packages using below commands
```
pip install -r requirement.txt
```
##Migrate the requied tables using below commands
```
python manage.py makemigrations walletapp
python manage.py migrate
```
##Run below command to load the fixtures. The below command will load the wallet types
```
python manage.py loaddata wallettype
```
##For frontend we are using vuetify framework to build the frontend run the below command
```
npm install
npm run build
```
##The above command will create dist folder in the current directory.
##To load the static files
```
python manage.py collectstatic
```
##After running all the above commands you can start the server using below command
```
python manage.py runserver 8012
```
##open the below link in browser
```
http://localhost:8012/wallet/
```

##API EndPoints :

## To get all wallettypes :
```
Method : GET
endpoint : /wallet/api/wallettype/
Example : http://localhost:8012/wallet/api/wallettype/
```
## To create wallettype :
```
Method : POST
endpoint : /wallet/api/wallettype/
payload : {
            "name": <wallet name>
          }
```

##To get user wallets :
```
Method : GET
End Point : /wallet/api/users/
Example : http://localhost:8012/wallet/api/users
```
##To Create wallet for the user :
```
Method : POST
End Point : /wallet/api/users/
payload : 
{
    "phonenumber": <mobile number>,
    "wallettype": <wallettype id>
}
Example : http://localhost:8012/wallet/api/users
```
##Credit money to the wallet
```
Method : POST
End Point : /wallet/api/transaction/credit/
payload : 
{
    "user": <UserObject ID>,
    "transactiontype": 'credit',
    "amount": <amount>
}
Example : http://localhost:8012/wallet/api/transaction/credit/
```
##Debit money to the wallet
MINIMUM WALLET BALANCE value is set to 1000 and it can configurable in settings.py file
```
Method : POST
End Point : /wallet/api/transaction/debit/
payload : 
{
    "user": <UserObject ID>,
    "transactiontype": 'debit',
    "amount": <amount>
}
Example : http://localhost:8012/wallet/api/transaction/debit/
```
##Get current balance for a user
```
Method : GET
End Point : /wallet/api/users/<phonenumber>/balance/
Example : http://localhost:8012/wallet/api/users/9878909098/balance/
```
##Retrieve the total amount credited and debited from a wallet within a specific time range
```
Method : GET
End Point : /wallet/api/users/transaction/?startdate=<StartDate>&enddate=<EndDate>
Example : http://localhost:8012/wallet/api/transaction/?startdate=2024-04-01&enddate=2024-04-31
```
