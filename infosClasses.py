classes_a_exclure = (
                    "cmoip.ICmoipCie",
                    "cmoip.ICmoipClient",
                    "cmoip.ICmoipClientCie",
                    "cmoip.ICmoipServerStandaloneCie",
                    "cmoip.ICmoipServerStandaloneSnmp",
                    "cmoip.ICmoipSnmp",
                    "ithTphAnnuaire.ICorrespExterne",
                    "mg2s.IAtelierEnergie",
                    "mg2s.IAtelierEnergieCie"
                    )

numeros_de_classe = {
### 1 Configuration (CMoIP)
    "system.IOperatingStateAbnormalStatusConfiguration":    "11",
    "mg2s.ISitePIUCie":                                     "12",
    "system.piu.IVersionAntiVirusSnmp":                     "13",
    "system.piu.IVersionAntiVirusCie":                      "14",
    "system.piu.IVersionElementSecretCie":                  "15", # vérifier le numéro
    "system.piu.IVersionElementSecretSnmp":                 "16", # vérifier le numéro
    "system.piu.IVersionSystemeSnmp":                       "17",
    "system.piu.IVersionSystemeCie":                        "18",
    "system.piu.IVersionTorrentCie":                        "19",
### 03 Configuration CDC
    "srsa.edcdc.shared.ICvr":                   "0300",
    "srsa.edcdc.shared.IToc":                   "0301",
    "srsa.edcdc.shared.ITocF":                  "0301",
    "srsa.edcdc.shared.IPageTov":               "0302",
    "srsa.edcdc.shared.IZoneTravail":           "0303",
    "srsa.edcdc.shared.IFrequence":             "0304",
    "srsa.edcdc.shared.IEqfFixe":               "0305",
    "srsa.edcdc.shared.IVoiePermanente":        "0306",
    "srsa.edcdc.shared.IProfilUtilisateur":     "0309",
    "srsa.edcdc.shared.IProfilRepli":           "0310",
    "srsa.edcdc.shared.IGroupeUtilisateurCdc":  "0311",
    "srsa.edcdc.IPlanRemplacement":             "0312",
    "srsa.edcdc.IPlanRemplacementAActiver":     "0313",
    "srsa.edcdc.shared.ICahierTOV":             "0314",
### 40 ITH-TPH Equipements
    "ithTphEquipements.ITsoip":                     "401",
    "ithTphEquipements.ITsoipServerStandalone":     "402",
    "ithTphEquipements.ITsoipServerStandaloneCie":  "403",
    "ithTphEquipements.IGatewaySTN":                "404",
    "ithTphEquipements.IModuleSTNFXS":              "405",
    "ithTphEquipements.ILigneFXS":                  "406",
### 41 POC - Configuration
    "pocConfiguration.IParametresGeneraux":         "411",
    "pocConfiguration.IDSCPSettings":               "413",
    "pocConfiguration.ILevelsVpoip":                "414",
    "pocConfiguration.ILevelsTsoip":                "414xx",
    "pocConfiguration.IEnregIpTsoipSettingsConf":   "415",
    "pocConfiguration.IMission":                    "416",
### 42 POC - Equipement
    "pocEquipement.IVPoIP":                     "421",
    "pocEquipement.IAudioProfiles":             "422",
### 43 ITH-TPH Configuration
    "ithTphConfiguration.IPrioritySettings":    "430",
    "ithTphConfiguration.IGfuIndex":            "431",
    "ithTphConfiguration.IGfu":                 "432",
    "ithTphConfiguration.IParamGenTph":         "433",
    "ithTphConfiguration.IPlanNumerotation":    "434",
    "ithTphConfiguration.IRestrictionsAppels":  "435",
    "ithTphAnnuaire.ITelProfil":                "436",
    "ithTphConfiguration.IDomains":             "437",
    "ithTphConfiguration.IConferenceMeetMe":    "438",
    "ithTphConfiguration.IFaisceau":            "439",
### 44 Annuaire
    "ithTphAnnuaire.IRole":                 "441",
    "ithTphAnnuaire.IGroupe":               "442",
    "ithTphAnnuaire.ICategorieCorresp":     "443",
    "ithTphAnnuaire.ICorrespExterne":       "444",
    "ithTphAnnuaire.ICei":                  "445",
    "ithTphAnnuaire.IContactExterneED137":  "446",
    "ithTphAnnuaire.IFOA":                  "447",
### 45 Cahiers de vue
    "ithTphCahiersDeVue.ILoop":             "451",
    "ithTphCahiersDeVue.IPageITH":          "452",
    "ithTphCahiersDeVue.IViewITH":          "453",
    "ithTphCahiersDeVue.IConference":       "454",
    "ithTphCahiersDeVue.IPageTPH":          "455",
    "ithTphCahiersDeVue.IViewTPH":          "456",
    "ithTphCahiersDeVue.IRegleView":        "457",
    "ithTphCahiersDeVue.IRegleViewDefault": "458",
### 50 Sites
    "mg2s.Region":                          "501",
    "mg2s.ISiteCDCSnmp":                    "502",
    "mg2s.ISiteCDCCie":                     "503",
    "mg2s.ISiteCERSnmp":                    "504",
    "mg2s.ISiteCERCie":                     "505",
    "mg2s.ISiteCOSCASnmp":                  "506",
    "mg2s.ISiteCOSCACie":                   "507",
    "mg2s.ISiteCMCCSnmp":                   "508",
    "mg2s.ISiteCMCCCie":                    "509",
    "mg2s.ISiteCCSnmp":                     "510",
    "mg2s.ISiteCCCie":                      "511",
    "cmoip.ICMoIPDistant":                  "512",
### 60 Switchs
    "mg2s.ISwitch4507CdcSnmp":          "601",
    "mg2s.ISwitch4507Snmp":             "602",
    "reseau.IStackOfSwitchSnmp":        "603",
    "reseau.ICisco2960X24PortsSnmp":    "604",
    "reseau.Cisco2960X24PortsCie":      "605",
    "reseau.ICisco2960X48PortsSnmp":    "606",
    "reseau.ISwitch48PortsCie":         "607",
    "reseau.ICisco365024PortsSnmp":     "608",
    "reseau.ICisco365048PortsSnmp":     "609",
    "mg2s.IModuleAlimentationSnmp":     "610",
    "mg2s.IModuleFibreSnmp":            "611",
    "mg2s.IModuleVentilateurSnmp":      "612",
    "reseau.IStackOf2SwitchSnmp":       "613",
    "reseau.IStackOf2SwitchCie":        "614",
    "mg2s.ISwitch4507CdcSnmp":          "6xx",
    "mg2s.ISwitch4507Snmp":             "6xx",
### 70 Radio
    "mg2s.IChassisSnmp":                        "701",
    "mg2s.ICarteMcrSnmp":                       "702",
    "mg2s.IAbstractChassisMcsSnmp":             "703",
    "mg2s.IAbstractChassisMcsCie":              "704",
    "mg2s.ICarteChassisCEXSnmp":                "705",
    "mg2s.ICarteChassisCEXCie":                 "706",
    "mg2s.ICarteChassisCERSnmp":                "707",
    "mg2s.ICarteChassisCERCie":                 "708",
    "mg2s.IPortMcrCommun":                      "709",
    "mg2s.IPortMcrMcsE1Snmp":                   "710",
    "mg2s.IPortMcrMcsE1Cie":                    "711",
    "mg2s.IPortMcrMcsEthSnmp":                  "712",
    "mg2s.IPortMcrMcsEthCie":                   "713",
    "mg2s.IPortMcrMcsPerSnmp":                  "714",
    "mg2s.IPortMcrMcsPerCie":                   "715",
    "mg2s.IPortMcrMcsS0Snmp":                   "716",
    "mg2s.IPortMcrMcsS0Cie":                    "717",
    "mg2s.IPortMcrMcsT2Snmp":                   "718",
    "mg2s.IPortMcrMcsT2Cie":                    "719",
### 80 Enregistreurs
    "vgoip.IVgoipEnregistreur":     "801",
    "vgoip.IVgoipRejeu":            "802",
    "vgoip.IVgoipSimulation":       "803",
    "mg2s.IVRoIPClusterSnmp":       "804",
    "mg2s.IVRoIPCoteSnmp":          "805",
    "mg2s.IVRoIPNoeudSnmp":         "806",
    "mg2s.IVRoIPServeurSnmp":       "807",
### 90 PERs
    "mg2s.IPerEmetteur":                        "901",
    "mg2s.IAbstractPerEmetteurCie":             "902",
    "mg2s.IPerEmetteurRecepteur":               "903",
    "mg2s.IAbstractPerEmetteurRecepteurCie":    "904",
    "mg2s.IPerEVFSnmp":                         "905",
    "mg2s.IPerEVFCie":                          "906",
    "mg2s.IPerRecepteur":                       "907",
    "mg2s.IAbstractPerRecepteurCie":            "908",
### 100 Multiplexeurs
    "mg2s.ICoupleur":                           "1001",
    "mg2s.ICoupleurCie":                        "1002",
### 110 Supervision
    "cmoip.ICmoipClient":                   "1101",
    "cmoip.ICmoipClientCie":                "1102",
    "cmoip.ICmoipSnmp":                     "1103",
    "cmoip.ICmoipCie":                      "1104",
    "cmoip.ICmoipServerStandaloneSnmp":     "1105",
    "cmoip.ICmoipServerStandaloneCie":      "1106",
### 120 Routeur
    "mg2s.IRouteur":                    "1201",
    "mg2s.IRouteurCie":                 "1202",
### 130 Gestion de ressources
    "mg2s.IFarCexSnmp":                 "1301",
    "mg2s.IFarCexCie":                  "1302",
    "mg2s.IFarCerSnmp":                 "1303",
    "mg2s.IFarCerCie":                  "1304",
    "mil.IARoIPLogiqueSnmp":            "1305",
    "mg2s.IARoIPLogiqueCie":            "13051",       # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerAnalogiqueMilitaireCie":   "130x",        # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerAnalogiqueMilitaireSnmp":  "130x",        # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerEd137MilitaireCie":        "130x",        # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerEd137MilitaireSnmp":       "130x",        # !!!!!!! numéro ?? !!!!!!!!
### 140 Serveurs
    "serveurs.IClusterUCGenerique":         "1401",
    "serveurs.IClusterUCGeneriquePIU":      "1401",
    "serveurs.IServeurSeducs":              "1402",
    "serveurs.IServeurUCGeneriqueSnmp":     "1403",
    "serveurs.IServeurUCGeneriquePIUSnmp":  "1403",
    "serveurs.IServeurUCGeneriqueCie":      "1404",
### 150 Parefeu
    "mg2s.IClusterDeNetasqSnmp":        "1501",
    "mg2s.IClusterDeNetasqCie":         "1502",
    "mg2s.IChiffreurHorsClusterSnmp":   "1503",
    "mg2s.IChiffreurHorsClusterCie":    "1504",
    "mg2s.ILiaisonVpnSnmp":             "1505",
    "mg2s.ILiaisonVpnCie":              "1506",
### 160 Collecteur alarmes
    "mg2s.IPeripheriqueCAMaitreSnmp":       "1601",
    "mg2s.IPeripheriqueCAMaitreCie":        "1602",
    "mg2s.IPeripheriqueCAEsclaveSnmp":      "1603",
    "mg2s.IPeripheriqueCAEsclaveCie":       "1604",
    "mg2s.IBoucleCASnmp":                   "1605",
    "mg2s.IBoucleCACie":                    "1606",
    "collecteur.alarmes.IOptoCie":          "1607",
    "collecteur.alarmes.IBoucleOptoCie":    "1608",
### 170 Atelier Energie
    "mg2s.IAtelierEnergie":         "1701",
    "mg2s.IAtelierEnergieCie":      "1702",
    "mg2s.IAtelierEnergieV7":       "1703",
    "mg2s.IAtelierEnergieV7Cie":    "1704",
### 180 Protections
    "mg2s.ICabine":             "1801",
    "mg2s.ILocalSnmp":          "1802",
    "mg2s.ILocalCie":           "1803",
    "mg2s.IBaieSnmp":           "1804",
    "mg2s.IBaieCie":            "1805",
### 190 Liens
    "port.ILienEth":                "1901",
    "port.ILienEthCie":             "1902",
### 200 Opto bic
    "collecteur.alarmes.IOptoSnmp":         "2001",
    "collecteur.alarmes.IBoucleOptoSnmp":   "2002",
### 230 VSoIP
    "mil.IVSoIP":               "2301",
    "mg2s.IVSoIPCie":           "23011",

### 240 PXoIP
    "mil.IPXoIPLogiqueSnmp":    "240",
    "mg2s.IPXoIPLogiqueCie":    "2401",
### 250 POoIP
    "mil.IPOoIPLogiqueSnmp":        "250",
    "mil.IPOoIPContainer":          "251",
    "mg2s.IPOoIPLogiqueCie":        "2501",
    "mil.IPOoIPContainerSnmp":      "2511",
### 260 VGoIP
    "mg2s.IChassisVGoIPCie":            "260x",     # !! numéro ?? !!
    "mg2s.IChassisVGoIPSnmp":           "260x",     # !! numéro ?? !!
    "mil.IMCRVGoIPCie":                 "260x",     # !! numéro ?? !!
    "mil.IMCRVGoIPSnmp":                "260x",     # !! numéro ?? !!
    "mil.IMiaeVGoIPCie":                "260x",     # !! numéro ?? !!
    "mil.IMiaeVGoIPSnmp":               "260x",     # !! numéro ?? !!
    "mg2s.IVGoIPDacCie":                "260x",     # !! numéro ?? !!
    "mil.IVGoIPDacSnmp":                "260x",     # !! numéro ?? !!
    "mg2s.IVGoIPServeurLogiqueCie":     "260x",     # !! numéro ?? !!
    "mil.IVGoIPServeurLogiqueSnmp":     "260x",     # !! numéro ?? !!
### 300 Silencieux
    "supervision.ISilencieuxCer":       "3001",
    "supervision.ISilencieuxCdcCie":    "3002",
### 310 Sécurité
    "securite.ICertificat":                     "3101",
    "securite.ICertificatCIE":                  "3102",
    "securite.ICertificatPFC":                  "3103",
    "securite.ICertificatRevocationList":       "3104",
    "securite.ICertificatRevocationListCIE":    "3105",
    "securite.ICertificatRevocationListPFC":    "3106",
    "securite.IIntegrityChecker":               "3107",
    "securite.IIntegrityCheckerCIE":            "3108",
    "securite.IVirusChecker":                   "3109",
    "securite.IVirusCheckerCIE":                "3110",
### 320 Autres
    "mil.IObjetDeSynthese":                 "3201",
    "mil.IAdpsServer":                      "3202",
    "mil.IPingSupervisedObject":            "3203",
    "mil.IAdpsSupervisedObject":            "3204",     # à vérifier
    "mg2s.IEquipementNonGere":              "3205",
    "system.IHttpServeur":                  "3206",
    "system.IPodmanContainer":              "3208",
    "mil.IInstanceApplicationMetierSnmp":   "3210",     # !! 32010 ?? !!
    "mil.IHttpServeurMilitaire":            "32061",
    "mil.IPodmanPodMilitaire":              "32071",
### 330 Configuration externe
    "mg2s.IConfigExterne":                  "3301",
    "mg2s.ISiteConfigExterne":              "3302",
    "mg2s.IZoneConfigExterne":              "3303",
### 340 Voies
    "supervision.IVoieRadioSnmp":           "3401",
    "supervision.IVoieRadioCie":            "3402",
    "supervision.IVoieCentreCorrelee":      "3403",
    "supervision.IVoieCentreSnmp":          "3404",
    "supervision.IVoieCentreCie":           "3405",
    "supervision.IVoieCentreParVoieRadio":  "3406",
    "supervision.IMission":                 "3407",
    "supervision.IMissionCOSCA":            "3408",
### 360 RDO-Configuration
    "rdoConfiguration.ICategorieVoie":          "3601",
    "rdoConfiguration.IEQF":                    "3602",
    "rdoConfiguration.IPageTOV":                "3604",
    "rdoConfiguration.IParametresGenerauxRDO":  "3605",
    "rdoConfiguration.IProfilRadioMg2s":        "3603",
### 
### 
    "site.IVoieParCentre": "xxx",

    "FIN": "999999999"
}
