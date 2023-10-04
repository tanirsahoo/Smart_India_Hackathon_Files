#terminal commands

#obv only root can do this stuff
#every group can have an administrator, password(no practical use) of its own and members

#/etc/passwd - all users and home directory info stored, user id, group id
#/etc/shadow - encrypted password stored(only sudo)
#also stored info abt last date of pass change, date of account expiry (non -encrypted)
#  * accounts are service accounts
#/etc/group - who belongs to which grp

#to modify these files use suo vipw or sudo vipr (-s - shadow)

#adding user
#only one user at a time
sudo adduser suku1 

#adding a group
#sudo groupadd -g 'Group-Id(>5000)' 'Group_Name'
sudo groupadd -g 21412 group1

#removing an user
sudo userdel suku1

#removing user with all their files and directory
sudo userdel -r suku1

#to add a user to a group(upto 15 groups possible)
#sudo usermod -G Group_name1,Group_name2... user_name
sudo usermod -G group1 suku1
#to modify the list of groups for a user, repeat with modified group names
#to remove a user from a group, mention the groups the user belongs to again

#there are many predefined groups in the system. which are primary groups
#what we are creating is secondary group

#to check which group the user belongs to
groups suku1

#to check who are the members of a group
getent group group1

#delete a group
sudo groupdel group1

#to give sudo privileges
sudo visudo
#add users with sudo priv

#when user deleted, mandatory to also remove its entry, if done, from visudo

#delete user
sudo deluser suku1