
### Automate Flask app deployment using Fabric python library easily
#### Required python version
```sh
$ python --version
Python 3.5.5
```
### Used Anaconda to virtual environment tool to separate app from others
#### Note: I believe that you have already installed anaconda in your server
#### Commands

##### Clone the repo
```sh
$ git clone https://github.com/<user>/<repo_name>.git
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
