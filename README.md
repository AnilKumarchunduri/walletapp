WalletApp prerequisites :

python >= 3.8, npm 14.x

##After installing the above packages you can run below commands :
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
##To Start the App in the docker run the below command :
```
git clone https://github.com/AnilKumarchunduri/walletapp.git
cd walletapp/
docker build -t walletapp:prd -f Dockerfile .
docker run -dt -p 8012:8012 --name walletapp walletapp:prd
```