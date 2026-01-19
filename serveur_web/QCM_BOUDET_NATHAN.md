# QCM – Évaluation Python & POO

Ce QCM vise à évaluer la compréhension de Python et de la Programmation Orientée Objet (POO)
à partir du code fourni (classes Message, WSClient, WSServer).

---

## Partie 1 – Concepts généraux Python & POO

### Question 1
Quel est le rôle principal de la classe `MessageType` ?

 
B. Simuler une énumération de types de messages  


---

### Question 2
Pourquoi `MessageType` n’hérite-t-elle pas de `Enum` ?


C. Parce qu’il s’agit d’un choix de conception simplifié  
  

---

### Question 3
Dans le constructeur de `Message`, que représente le paramètre `receiver=None` ?


C. Un paramètre optionnel avec valeur par défaut  

---

## Partie 2 – Méthodes et encapsulation

### Question 4
Quel est l’intérêt de la méthode statique `default_message()` ?


C. Fournir une instance par défaut de `Message`  
  

---

### Question 5
Pourquoi `default_message()` est-elle décorée avec `@staticmethod` ?

 
B. Elle agit sur la classe et non sur une instance  
 

---

### Question 6
Quel problème potentiel existe dans `default_message()` ?

A. Le type du message n’est pas cohérent avec `MessageType`  
B. Le JSON est mal formé  
C. La méthode n’est jamais appelée  
 

---

## Partie 3 – Sérialisation JSON

### Question 7
Quel est le rôle de la méthode `to_json()` ?

 
C. Convertir un message en chaîne JSON  

---

### Question 8
Pourquoi `import json` est-il placé à l’intérieur des méthodes ?

A. Pour réduire la portée de l’import  
  
 

---

### Question 9
Que fait la méthode `from_json()` ?


B. Elle crée une instance de `Message` à partir d’une chaîne JSON  
 

---

### Question 10
À quoi sert l’instruction `assert` dans ce code ?


B. Tester l’égalité logique de deux messages  


---

## Partie 4 – WebSocket Client

### Question 11
Quel est le rôle principal de la classe `WSClient` ?

 
  
C. Se connecter à un serveur WebSocket et échanger des messages  

---

### Question 12
Pourquoi les méthodes `on_open`, `on_message`, etc. sont-elles passées au constructeur de `WebSocketApp` ?

  
B. Pour être appelées automatiquement lors des événements WebSocket  
 

---

## Partie 5 – WebSocket Server

### Question 13
Quel est le rôle de la classe `WSServer` ?


B. Gérer plusieurs clients WebSocket  
  
D. Tester le client  

---

### Question 14
Pourquoi utilise-t-on des méthodes statiques `dev()` et `prod()` ?

  
B. Pour fournir des configurations différentes du serveur  
  

---

### Question 15
Quel principe POO est principalement illustré par les classes `WSClient` et `WSServer` ?

A. Héritage  
  

---

## Bonus – Question ouverte

### Question 16
Citez deux améliorations possibles à apporter à ce code (structure, robustesse, typage, sécurité, etc.).

---

**Fin du QCM**
