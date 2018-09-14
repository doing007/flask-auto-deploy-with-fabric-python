
### Automate Flask app deployment using Fabric python library easily
#### Required python version
```sh
$ python --version
Python 3.5.5
```
### Used Anaconda to virtual environment tool to separate app from others
#### Note: I believe that you have already installed anaconda in your server
#### Commands

#### First *IMPORTANT* thing to do is Generating SSH key and add it to the Github Account
Here is the [link](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
AND
Add your ssh key to Authorised Access keys list in the server, so that It wont ask for the password

##### Clone the repo
```sh
$ git clone https://github.com/<user>/<repo_name>.git
OR
$ git clone git@github.com:<USER>/<REPO_NAME>.git
```
##### Create virtual environment (Install Anaconda before running this command)
```sh
$ conda env create -f flask_auto_deploy.yml
```
### Or
#### Create new virtual env using `conda create -n env_name python=3.5`

##### Activate the virtual env
```sh
$ source activate env_name
```
##### Install `requirements.txt`
```sh
$ pip install -r requirements.txt
```
#### Once All this done, now you should be able to see some available commands with `fab`

##### To see the list of command
```sh
$ fab --list
```

##### To check the service status. example
```sh
$ fab service nginx status
```
