# 📊 Suivi du Bitcoin en Temps Réel

Cette application **Streamlit** permet de suivre le prix du Bitcoin en temps réel et d'afficher des graphiques interactifs sur différentes périodes.

## 🚀 Fonctionnalités
- 📈 **Graphique en courbe avec points** indiquant les prix du Bitcoin
- 🕯 **Graphique en chandeliers (candlestick)** pour une meilleure analyse technique
- ⏳ Sélection de la période : **7 jours, 30 jours, 90 jours, 1 an, 3 ans**
- 🔄 Bouton de **rafraîchissement** des données
- 💰 Affichage du **prix actuel du Bitcoin** en EUR

## 🛠️ Installation
### 1️⃣ Cloner le dépôt
```sh
git clone https://github.com/ri2az/BTC.git
cd BTC
```

### 2️⃣ Installer les dépendances
Assurez-vous d'avoir Python 3 installé, puis exécutez :
```sh
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application
```sh
streamlit run app.py
```

### 4️⃣ Lancer l'application sur Streamlit !

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://riaaz-btc.streamlit.app/)

## 📡 API Utilisée
L'application utilise l'API **CryptoCompare** pour récupérer :
- 📌 Le **prix actuel** du Bitcoin : `https://min-api.cryptocompare.com/data/price`
- 📌 Les **données historiques** du Bitcoin : `https://min-api.cryptocompare.com/data/v2/histoday`

Cette API ne nécessite **pas de clé d'API**, ce qui la rend simple d'utilisation !


## ⚙️ Technologies utilisées
- **Python 3** 🐍
- **Streamlit** 🖥️ (interface utilisateur)
- **Plotly** 📊 (visualisation des graphiques)
- **Pandas** 📄 (gestion des données)
- **Requests** 🌐 (récupération des données depuis l'API)

## 📜 Licence
Ce projet est sous licence **MIT**. Vous pouvez le modifier et l'utiliser librement.

## 🤝 Contribuer
Vous souhaitez améliorer ce projet ? Voici comment :
1. **Forkez** le dépôt 🍴
2. **Créez une branche** (`git checkout -b feature-ma-fonctionnalite`)
3. **Commitez vos changements** (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. **Pushez la branche** (`git push origin feature-ma-fonctionnalite`)
5. **Créez une Pull Request** ✅

---
🔥 **Développé pour les amateurs de crypto !** 🚀

