1) ## Avoir la version 3.12.4 de python installer sur votre machine


2) ## une fois dans le dossier projet en invite de commande, exécuter la commande "env\Scripts\activate

* cette commande permet d'activer l'environement virtuel

[Exemple] D:\ProjetsPro\data-sciences\projet>env\scripts\activate

vous verez ceci après : *(env) D:\ProjetsPro\data-sciences\projet>*

3) ## exécuter en suite la commande "pip install -r requirements.txt" pour installer les dependances du projet : il faut avoir une bonne connexion stable

[Exemple] (env) D:\ProjetsPro\data-sciences\projet>pip install -r requirements.txt

## migrer vers le dossier API
[Exemple] (env) D:\ProjetsPro\data-sciences\projet>cd API   

## resultat après
[Exemple] (env) D:\ProjetsPro\data-sciences\projet\API>

## lancer le projet Flask qui represente l'API
[Exemple] (env) D:\ProjetsPro\data-sciences\projet\API>flask run

(env) D:\ProjetsPro\data-sciences\API>flask run

## Vous obtenez le resultat ci dessous qui montre que l"API a été bien lancé et tourne sur l'adresse http://127.0.0.1:5000

 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

## Vous pourrez donc faire des requestes dessus

## Ci-dessous les champs à renseigner depuis votre frontend dans un fichier en respectant bien les types: str pour chaine de caractère

    Timestamp: str
    SourceIPAddress: str
    DestinationIPAddress: str
    SourcePort: float
    DestinationPort: float
    Protocol: str
    PacketType: str
    PacketLength: float
    TrafficType: str
    AnomalyScores: float
    AttackType: str
    AttackSignature: str
    ActionTaken: str
    SeverityLevel: str
    NetworkSegment: str
    FirewallLogs: str
    LogSource: str