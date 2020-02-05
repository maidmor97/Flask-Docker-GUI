#!/usr/bin/env python3
'''
Entry point for the flask backend
'''
import connexion

connexionApp = connexion.App(__name__, specification_dir='./')
connexionApp.add_api('openapi.yaml', arguments={'title': 'Flask-Docker GUI Backend '}, pythonic_params=True)

app = connexionApp.app

if __name__ == '__main__':
    app.run(port=8080)
