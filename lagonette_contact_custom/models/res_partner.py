from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    date_out = fields.Date(string='exit date') #Date de sortie
    legal_status = fields.Selection([('association','Association'),
                                ('sarl','SARL'),('eurl','EURL'),
                                ('sas','SAS'),('sasu','SASU'),
                                ('sa','SA'),
                                ('sca','SCA'),
                                ('scop_sarl','SCOP SARL'),
                                ('scop_sas','SCOP SAS'),
                                ('scop_sa','SCOP SA'),
                                ('scic_sarl','SCIC SARL'),
                                ('scic_sas','SCIC SAS'),
                                ('scic_sa','SCIC SA'),
                                ('scic_cae','SCIC CAE'),
                                ('profession_liberale','Profession libérale'),
                                ('entreprise_individuelle','Entreprise individuelle'),
                                ('collectivite','Collectivité'),
                                ('fondation','Fondation'),
                                ('salariee_cooperative','Salarié.e Coopérative'),
                                ('gaec','GAEC')],
                                string='legal status') #Statut juridique
    naf = fields.Char(string='NAF')#NAF
    ref_volunter = fields.Char(string='volunteer referent')#Référent bénévole
    source = fields.Selection([('demarche_spontanee','Démarche spontanée'),
                        ('demarche_de_notre_part','Démarche de notre part'),
                        ('event_fb_lyon_en_commun','Event FB Lyon en commun'),
                        ('nef','NEF'),
                        ('cigales','Cigales'),
                        ('recommandation_dun_pro','Recommandation d\'un pro'),
                        ('recommandation_d_un_utilisateur','Recommandation d\'un utilisateur'),
                        ('autre','Autre'),
                        ('outil_de_collecte_et_de_redistriution_des_sous','Outil de collecte et de redistriution des sous')],
                        string='source') #Origine de la démarche
    track_record_pro = fields.Char(string='track record pro') #Lien suivi
    why_out = fields.Selection(	[('autre','Autre'),
                            ('raison_non_précisee','Raison non précisée'),
                            ('pas_assez_de_gonettes_reçues_manque_de_dynamique_locale', 'Pas assez de gonettes reçues/manque de dynamique locale'),
                            ('perte_de_sens_pour_le_projet',"Perte de sens ou d'intérêt pour le projet"),
                            ('Raisons_independantes_gonette', 'Raisons indépendantes à la Gonette (déménagement, cessation de l\'activité etc...)'),
                            ('Difficulte_de_gestion_comptabilite', 'Difficulté de gestion/comptabilité'),
                            ('difficulte_a_ecouler_les_gonettes','Difficulté à écouler les gonettes'),
                            ('gros_retard_de_cotisation','Gros retard de cotisation')],
                            string='why out') #Raison du départ