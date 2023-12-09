# Policies
Name | Scripts | Status
-----|---------|--------
1.Access management | tor script,ssh script | Confirmed
2.Data protection policy | password schema, Firewall and other network scripts,Encrytion scripts) | In progress
3.Hardware policy | USB script | Confirmed
1.Access management policy | (tor script,ssh script) | Confirmed
2.Data protection policy | (password schema,Firewall and other network scripts,Encrytion scripts) | In progress
3.Hardware policy | (USB script) | Confirmed
4.IDS policy | LIDS(log based) script | Holding
5.Application whitelisting policy | _ | Holding
6.Roles and responsibilities policy | (Admin,users,login script) | Confirm


# Guideline how we are going to integrate the GUI.
1. There are 5 frames we have discussed so far, they are:
    1. The Policies page
    2. The User list
    3. The implemented policies list on a selected user.
    4. On Clicking the implement button a window appears showing animation( Implementing a hardening script for the whole system might take some time. During that crucial seconds we will run a funny animation.)
    5. The implemented policies list but the upgraded version.
2. To do list:
   1. We have developed the script to find the number of directories in the /home folder which directly indicates the number of active accounts/users in the server/system.
   2. The script will provide the name of the users in the form of an array.
   3. Integrate this script with the 2nd frame discussed above.
