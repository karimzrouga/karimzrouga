# Mise à jour du profil GitHub — branche prod

Le dépôt public doit être nommé `karimzrouga/karimzrouga`. Son README à la racine est affiché sur le profil. Choisis `prod` comme branche par défaut dans les paramètres GitHub du dépôt si tu utilises cette branche.

1. Extrais le ZIP sur le Bureau : il contient le dossier `karimzrouga-profile-update`.
2. Ferme les aperçus éventuels, puis ouvre CMD. Copie les fichiers dans ton dépôt existant avec les commandes ci-dessous. Le dossier `.github` est inclus.

```bat
cd /d C:\Users\hp\Desktop\karimzrouga-profile
git switch prod
robocopy "C:\Users\hp\Desktop\karimzrouga-profile-update" "." /E /XD .git __pycache__
if exist assets\karim-anime-wave.svg del assets\karim-anime-wave.svg
if exist assets\karim-anime-warrior.svg del assets\karim-anime-warrior.svg
git status
git add README.md INSTALLATION.md CREDITS.md preview.html assets scripts .github
git commit -m "Replace profile characters with supplied video and photo"
git push -u origin prod
```

Si `prod` n’existe pas localement mais existe sur GitHub : `git fetch origin` puis `git switch --track origin/prod`. Si tu souhaites créer cette branche : `git switch -c prod`.

Si Git demande ton identité :
```bat
git config user.name "Mohamed Karim Zrouga"
git config user.email "TON_EMAIL_GITHUB"
```
Remplace le texte par ton email vérifié GitHub ou ton adresse privée noreply indiquée dans GitHub → Settings → Emails, puis relance le commit et le push.

## Médias

- Première section : `assets/hero.gif`, rendu à partir de la vidéo fournie, en boucle et sans son dans le README.
- Vidéo originale conservée : `assets/karim-wave.mp4`. `preview.html` utilise ce MP4 en lecture automatique muette, en boucle, avec commandes.
- Autres sections : ta photo intégrée aux SVG `about.svg`, `id-dashboard.svg` et `connect.svg`, y compris les deux emplacements de présentation. `assets/karim-photo.png` conserve l’image originale.
- `hero-background.svg` contient la mise en page de la première section ; `hero.svg` est son aperçu fixe avec la première image vidéo.
- Les animations de section existantes sont conservées ; l’ancienne animation du personnage et le guerrier ont été supprimés.

Ouvre `preview.html` pour vérifier localement. Ensuite lance Actions → Update profile → Run workflow sur `prod` pour les statistiques et la ville. Le workflow utilise GITHUB_TOKEN avec permission d’écriture. La planification quotidienne suit la branche par défaut. Les chiffres en attente seront remplacés à la première exécution.

`robocopy` renvoie normalement un code de 0 à 7 en cas de réussite ; 8 ou plus indique une erreur. Il copie les fichiers sans effacer ton dossier Git.

## Nouveautés — loisirs et contributions

La section loisirs présente six scènes SVG, chacune visible six secondes : Food, Gym, Cycling, Camping, Coding, Running. Les icônes bougent indépendamment ; en mode de réduction des mouvements, seule la première scène est affichée.

Le calendrier 3D utilise le même générateur que le dépôt de référence, avec tes couleurs bleu/violet. Il inclut une répartition des langages, un radar d’activité et une animation de croissance. `scripts/contrib-settings.json` configure son thème. Le workflow est fixé à une révision précise du générateur.

Après le push sur `prod`, le workflow se lance automatiquement si son fichier ou un script a changé. Tu peux aussi utiliser Actions → Update profile → Run workflow → prod. Le visuel fourni affiche un état en attente jusqu’à la première génération ; aucun chiffre de démonstration n’est présenté comme réel. Le résultat remplace automatiquement `assets/city.svg`.

## Si les contributions restent en attente

Vérifie que `.github/workflows/update-profile.yml` est présent dans le dépôt. Cette version se lance à chaque push sur `prod` ou `main`, sans filtre de chemins. La génération 3D est tentée même si la récupération des statistiques échoue.

Sur GitHub : Actions → Update profile → ouvre la dernière exécution. Un état rouge nécessite de lire le message de l’étape en erreur. Pour lancer manuellement et pour la planification quotidienne, le workflow doit être présent sur la branche par défaut ; utilise `prod` comme branche par défaut si c’est ta branche de travail. Après une exécution réussie, fais `git pull --rebase origin prod` avant tes prochaines modifications : le bot aura ajouté un commit.

La scène Gym est désormais explicitement nommée Musculation, avec un personnage et une barre. Elle apparaît pendant le deuxième intervalle du carrousel (environ 6 à 12 secondes après le début).
