# Foodyyy-Restaurant

#Install and Activate Virtual-environment

 pip install virtualenv
 virtualenv your_environment_name
 cd your_environment_name
./scripts/activate

#Import project in virtualenv
git clone https://github.com/Shehbaazsk/Foodyyy-Restaurant.git

To use that app
1.Create a env file and add DEBUG=True,SECRET_KEY= Any string you want or you can generate one with "python -c "import secrets; print(secrets.token_urlsafe())"
and last add DATABASE_URL="any database that Django supports"

2.Install all requirement packages with " pip install -r requirements.txt"

# Run Project
python manage.py runserver
