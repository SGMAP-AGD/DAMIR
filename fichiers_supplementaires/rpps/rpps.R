# http://www.data.drees.sante.gouv.fr/TableViewer/tableView.aspx
# https://www.data.gouv.fr/fr/datasets/la-demographie-des-medecins-rpps/
# Effectifs des médecins par spécialité, mode d’exercice et zone d’inscription
# Mise en forme des données
rpps <- read.csv2("data/2014-01-rpps-tab3-v3_75220837517610.csv", 
                  skip = 2, 
                  fileEncoding = "latin1", 
                  stringsAsFactors = FALSE)

names(rpps) <- c("mode_exercice", "zone_inscription", "annee", "specialite", "effectifs")
write.table(rpps, file = "data/rpps_tab3.csv", row.names = FALSE, sep = ",", dec = ".")
