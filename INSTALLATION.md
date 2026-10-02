# Profil GitHub animé — pack complet

1. Crée ou ouvre le dépôt public `karimzrouga/karimzrouga`.
2. Copie le CONTENU du dossier `karimzrouga-profile` à la racine du dépôt, y compris `.github/`.
3. Commit sur la branche par défaut.
4. Ouvre **Actions → Update profile → Run workflow**. GitHub génère les statistiques et la ville, puis les actualise chaque jour. Aucun token personnel à fournir : le workflow utilise GITHUB_TOKEN.
5. Ouvre `preview.html` dans ton navigateur pour voir le profil complet localement.

## Contenu

- `README.md` : profil et projets.
- `assets/hero.svg` : personnage anime qui salue, rôles et effets lumineux.
- `assets/about.svg` : présentation et carousel avec personnage guerrier.
- `assets/stack.svg` : orbite et grille de technologies.
- `assets/id-dashboard.svg` : badge suspendu avec personnage anime.
- `assets/connect.svg` : personnage anime et cartes de contact.
- `assets/karim-anime-wave.svg` et `assets/karim-anime-warrior.svg` : personnages autonomes réutilisables.
- `assets/stats.svg` et `assets/city.svg` : données produites par le workflow.
- `scripts/update_profile.py` et `.github/workflows/update-profile.yml` : actualisation quotidienne.

Les deux nouveaux personnages sont vectoriels sur fond transparent. Ils utilisent des tracés et des animations CSS, sans photo embarquée ni JavaScript. Les SVG des sections intègrent les personnages directement : pas de dépendance externe pour leur affichage.

Le premier personnage salue et cligne des yeux ; le second incline légèrement la tête et cligne des yeux. La respiration est stylisée. Les animations sont désactivées si le navigateur demande de réduire les mouvements. Les sections de référence conservent aussi des animations SMIL qui peuvent continuer selon le lecteur SVG.

Le rendu statique peut être affiché par certains lecteurs ; ouvre les SVG dans un navigateur pour voir les mouvements. Si GitHub sert une ancienne image, incrémente le paramètre `?v=5`. La ville et les statistiques restent en attente jusqu’à la première exécution réelle du workflow.

Si la branche est protégée, ses règles doivent autoriser le commit du bot pour actualiser les images.

Attribution du modèle : CREDITS.md.
