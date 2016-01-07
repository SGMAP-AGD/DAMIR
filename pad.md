
   * *aHackathon 26/01 - Données de santé DAMIR **Inscrivez ci-dessous vos idées de sujets :*


**- Va-t-on plus chez le médecins lorsque l'offre de médecins est plus  élevée ? **
  - En croisant le DAMIR, les données de démographie des médecins et  des données sur la population des assurés, on regardera si la densité de  médecins par habitant a des effets sur le nombre d'actes par assuré.
   La  difficulté du sujet vient du fait que la densité de médecin peut elle  même dépendre de variables inobservées comme l'état de santé de la  population locale ou plus généralement la propension de la population  locale à aller chez le médecin). 
   On essaiera de trouver des stratégies  pour identifier l'effet de l'offre de médecins sur le nombre d'actes par  assuré. 
  - Porteur du projet : Paul-Antoine Chevalier (Etalab,  paul-antoine.chevalier@data.gouv.fr) 

**- Peut-on faire un lien entre l'offre de soins (intensité concurrentielle) et la pratique du dépassement d'honoraire ?   **
  - Peut-on établir un lien entre la densité de médecins par spécialité  et par territoire et la pratique du dépassement d'honoraires ? Est-ce  dans les territoires où la densité est la plus forte que les médecins  pratiquent le moins les dépassement d'honoraires ?
   Peut-on identifier  l'effet de l'offre de soins indépendamment de l'effet de la demande. 
  - Porteur du projet : Paul Bouchequet

**- Quels sont les risques de réidentification des individus ? **
  - Il est important de garantir que les données ouvertes ne puissent  pas donner lieu à une réidentification des individus (assurés ou  professionnels de santé). 
  En particulier, on pourra explorer les  possibilités de réidentification des professionnels de santé en croisant  les données du DAMIR avec la démographie des professionnels de santé. 
  - Porteur du projet : Etalab

* Comparer, par département, pour chaque type d'acte, pour chaque tranche d'age, le ratio du nombre d'acte sur le nombre d'habitants de cette tranche d'age (données population). On s'attend à priori à ce que chaque type d'acte ait le même profil de ratio en fonction de l'âge. Ce qui est intéressant serait de repérer les anomalies (ex fictif: dans le 91, les jeunes constituent la moitié des actes d'orthopédie alors que c'est 1/4 ailleurs) et de les expliquer (plus dûr...). L'objectif serait de repérer des "hot-spots" où les jeunes sont beaucoup plus touchés par certains problèmes, pour suggérer qu'il y a des facteurs aggravants dans ces départements. Faire éventuellement une cartographie. (Leo Bouloc)

**Une sous-consommation de la médecine de ville est-elle géographiquement corrélée avec une surconsommation des urgences ?**
Nous venons avec des analyses assez fines du PMSI pour repérer des surconsommations d’urgence et espérons que le jeu de données sera suffisamment fin géographiquement (soit à un niveau infra-départementale) pour évaluer une sur/sous consommation des soins de ville 
Porteur : Matthieu LOUIS / GE Healthcare Partners

**Les complémentaires et l’assurance maladie ont-elles intérêt à financer la lutte contre la désertification médicale … jusqu’à quel niveau**
Là encore, suppose un jeu de données plus précis géographiquement, sur le patient et le praticien.
L’idée est de savoir si les complémentaires auraient intérêt à financer l’installation de médecins dans des zones moins couvertes pour faire dégonfler la facture en transport et en dépassement d’honoraire
Porteur : Matthieu LOUIS / GE Healthcare Partners

**- Observe-t-on une corrélation entre dépenses médicales et indicateurs de l'état de santé comme le niveau d'activité et l'IMC ?**
  - En croisant les données DAMIR départementales avec des données agrégées issues des objets connectés Withings, l'idée est de voir si dans les départements où la dépense per capita est élevée l'on observe des tendances quant au :
      - Taux d'individus en surpoids ou obèses
      - Niveau d'activité, mesuré en nombre moyen de pas réalisés par jour
Porteurs : Angela Chieh \& Pierre Duquesne (Withings)

On est mal car il y a pas la moindre données géographique dans le fichier, on est limités aux actes (NGAP et CCAM)et médicaments remboursés, à la spécialité du prescripteur et de l'exécutant, au taux de remboursement :/
a part le défi 3 je vois pas comment travailler sur les autres. => Si, il y a des données géographiques pour les données mises à disposition demain : détail du département pour les prescripteurs et 9 zones géographiques pour l'OpenDAMIR.  => cool on pourra l'avoir chargé dans OpenDataSoft ?
par contre on peut analyser les actes les +/- remboursés par spécialités, les médicaments +/- remboursés par spécialités
Développeur : Sébastien Letélié (Hacking Health)

**- Quel taux de fuite des français dans les pays étrangers ?**
A l’aide des données de remboursement des soins à l’étranger départementalisées dans les DAMIR, un taux de fuite sera calculé permettant de valider si la taux de fuite est plus important pour les français frontaliers, créant ainsi un indicateur de la qualité du système de santé français face à la demande
Porteur : Thomas Micheneau (jalma)

**Explorer la thématique de traitement de l'alcoolisme, en explorant le DAMIR pour voir s'il peut apporter des informations sur l'explication de tels phénomènes.**
Porteur : OpenHealth - Celtipharm

**Croisement population (INSEE, IDH2)**
Porteur : Julien Rutard - CapgeminiConsulting

**Cartographie interactive en terme de permanence des soins**
Porteur : Service statistique - Ministère de l santé


**Comparaison dans les campagnes de despistage cancer entre le depistage organisé et le dépistage individuel**
Porteur : Guillaume Janerau


**Estimer les Restes à Charges après remboursement de l'Assurance Maladie : ce qui est laissé à la charge des assurés et/ou des Complémentaires;** 
**[en fonction du régime exonérant de l'assuré : ce qui est pris en charge à 100% versus ce qui n'est pas pris en charge à 100%]** 

- en mesurant l'évolution dans le temps, 
- par situations géographique, 
- par nature de prestations ou de prestataires de soins 
- mesurer la concentration ou la dispersion des RAC sur les assurés

2 variables d’attaque :
-          Motif d’exonération : EXO\_MTF
-          Taux de remboursement 
 
Axes d’analyse :
-          Zone géographique
-          Par Age
-          Par typologie d’actes-          Par spécialistes/médecin exécutants
-          Par type d’établissements

Porteur COVEA (MMA/MAAF/GMF) T.LEMELE/ O. TAPIN/ N. BARRE/ L. BROUDOUX/ Y. GUILLERM

**Etude de quelques caractéristiques de l'ensemble des actes d'hépato-gastroentérologie :**
- tendance générale pluri-annuelle (2010-2013),
- saisonalité mensuelle,
- spécialités liées (en prescription ou en exécution),
- taux de remboursement réel en fonction du taux de remboursement théorique,
dans une logique exploratoire et d'apprentissage des bases mises à disposition.
Puis généralisation à l'ensemble des spécialités.
Ressources utilisées :
- fichiers N (disponibles sur Etalab),
- R, QlikView.
Equipe projet ANAP : Aude Schindler, Dominique Lepère, Philippe Gérard-Dematons

