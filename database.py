from firebase import firebase

firebase = firebase.FirebaseApplication("https://caixa-comport.firebaseio.com/", None)
data = {
    "number": number
    "name": name
    "start": start
    "finish": finish
    "nosepoke": nosepoke
    "leverPress": leverPress
    "leverSide": leverSide
}

firebase.post("/caixa-comport/Rats", data)

result = firebase.get("/caixa-comport/Rats", "")
   

''' 
Criacao de regras...
Tornar chaves os campos name e number. ".validate" nao esta terminada, pois eh preciso ver real utilidade da mesma

{
  "rules": {
    "Rats": {
      ".indexOn": ["number", "name"],
      ".validate": "newData.hasChildren(['number', 'name', 'start', 'finish', ]) && newData.child('content').isString() && newData.child('timestamp').isNumber()"
    }
  }
}

'''
