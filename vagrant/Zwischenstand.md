# Aktueller Stand Privacyscore lokal laufen lasse 
Aktueller Stand nach 3 Tagen prototyping. 
## Anforderungen
- Vagrant mit pass lookup plugin und virtualbox
- Ansible 2.7 oder neuer
- Python 3
- ansible-galaxy install geerlingguy.postgresql
## Lokal Aufsetzen
- Git auschecken
- Readme.md vom Projekt beachten (also password Stores anlegen und SSH Key an die richtigen stellen legen. `vagrant/provisioning/id_rsa`)
- Im Lokalen Browser auf dem Host http://ps-gronau-it-master.local aufrufen

## ToDo
Jede Menge...
Aktuell läuft z.B. das Verarbeitung der Reports noch nicht richtig. 
- Zuerst sollte man das Ansible Zeug ohne Fehler und Warnings gleich beim ersten vagrant up durchlaufen lassen können. 
- Dann muss man sich genauer anschauen, warum die Verarbeitung der Reports nicht läuft. 
- Dann muss man z.B. Terraform verwenden und mal gegen VMware und AWS deployen
- Theming und verbesserung der ganzen Anwendung muss dann auch folgen. 
- Ansible in saubere Rollen überführen und Datenhaltung separieren
- Letsencrypt ermöglichen
- URL dynamisch machen. 



