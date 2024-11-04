classes_a_exclure = (
                    "cmoip.ICmoipClient", "cmoip.ICmoipClientCie",
                    "cmoip.ICmoipServerStandaloneSnmp", "cmoip.ICmoipServerStandaloneCie",
                    "cmoip.ICmoipSnmp", "cmoip.ICmoipCie",
                    "ithTphAnnuaire.ICorrespExterne",
                    "mg2s.IAtelierEnergie", "mg2s.IAtelierEnergieCie",
                    "ithTphEquipements.ITsoipServerStandalone", "ithTphEquipements.ITsoipServerStandaloneCie"
                    )

numeros_de_classe = {
### 1 Configuration (CMoIP)
    "system.IOperatingStateAbnormalStatusConfiguration":    { 'numero': "11", 'dossier': "1_configurationCmoip" },
    "mg2s.ISitePIUCie":                                     { 'numero': "12", 'dossier': "1_configurationCmoip" },
    "system.piu.IVersionAntiVirusSnmp":                     { 'numero': "13", 'dossier': "1_configurationCmoip" },
    "system.piu.IVersionAntiVirusCie":                      { 'numero': "14", 'dossier': "1_configurationCmoip" },
    "system.piu.IVersionElementSecretCie":                  { 'numero': "15", 'dossier': "1_configurationCmoip" },      # vérifier le numéro
    "system.piu.IVersionElementSecretSnmp":                 { 'numero': "16", 'dossier': "1_configurationCmoip" },      # vérifier le numéro
    "system.piu.IVersionSystemeSnmp":                       { 'numero': "17", 'dossier': "1_configurationCmoip" },
    "system.piu.IVersionSystemeCie":                        { 'numero': "18", 'dossier': "1_configurationCmoip" },
    "system.piu.IVersionTorrentCie":                        { 'numero': "19", 'dossier': "1_configurationCmoip" },
### 03 Configuration CDC
    "srsa.edcdc.shared.ICvr":                   { 'numero': "0300", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IToc":                   { 'numero': "0301", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.ITocF":                  { 'numero': "0301", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IPageTov":               { 'numero': "0302", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IZoneTravail":           { 'numero': "0303", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IFrequence":             { 'numero': "0304", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IEqfFixe":               { 'numero': "0305", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IVoiePermanente":        { 'numero': "0306", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IProfilUtilisateur":     { 'numero': "0309", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IProfilRepli":           { 'numero': "0310", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IGroupeUtilisateurCdc":  { 'numero': "0311", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.IPlanRemplacement":             { 'numero': "0312", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.IPlanRemplacementAActiver":     { 'numero': "0313", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.ICahierTOV":             { 'numero': "0314", 'dossier': "03_configurationCdc" },
    "srsa.edcdc.shared.IVoieStatic":            { 'numero': "0315", 'dossier': "03_configurationCdc" },
### 40 ITH-TPH Equipements
    "ithTphEquipements.ITsoip":                     { 'numero': "401", 'dossier': "40_ithTphEquipement" },
    "ithTphEquipements.ITsoipServerStandalone":     { 'numero': "402", 'dossier': "40_ithTphEquipement" },
    "ithTphEquipements.ITsoipServerStandaloneCie":  { 'numero': "403", 'dossier': "40_ithTphEquipement" },
    "ithTphEquipements.IGatewaySTN":                { 'numero': "404", 'dossier': "40_ithTphEquipement" },
    "ithTphEquipements.IModuleSTNFXS":              { 'numero': "405", 'dossier': "40_ithTphEquipement" },
    "ithTphEquipements.ILigneFXS":                  { 'numero': "406", 'dossier': "40_ithTphEquipement" },
### 41 POC - Configuration
    "pocConfiguration.IParametresGeneraux":         { 'numero': "411", 'dossier': "41_pocConfiguration" },
    "pocConfiguration.IDSCPSettings":               { 'numero': "413", 'dossier': "41_pocConfiguration" },
    "pocConfiguration.ILevelsVpoip":                { 'numero': "414", 'dossier': "41_pocConfiguration" },
    "pocConfiguration.ILevelsTsoip":                { 'numero': "414xx", 'dossier': "41_pocConfiguration" },
    "pocConfiguration.IEnregIpTsoipSettingsConf":   { 'numero': "415", 'dossier': "41_pocConfiguration" },
    "pocConfiguration.IMission":                    { 'numero': "416", 'dossier': "41_pocConfiguration" },
### 42 POC - Equipement
    "pocEquipement.IVPoIP":                     { 'numero': "421", 'dossier': "42_pocEquipement" },
    "pocEquipement.IAudioProfiles":             { 'numero': "422", 'dossier': "42_pocEquipement" },
### 43 ITH-TPH Configuration
    "ithTphConfiguration.IPrioritySettings":    { 'numero': "430", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IGfuIndex":            { 'numero': "431", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IGfu":                 { 'numero': "432", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IParamGenTph":         { 'numero': "433", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IPlanNumerotation":    { 'numero': "434", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IRestrictionsAppels":  { 'numero': "435", 'dossier': "43_ithTphConfiguration" },
    "ithTphAnnuaire.ITelProfil":                { 'numero': "436", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IDomains":             { 'numero': "437", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IConferenceMeetMe":    { 'numero': "438", 'dossier': "43_ithTphConfiguration" },
    "ithTphConfiguration.IFaisceau":            { 'numero': "439", 'dossier': "43_ithTphConfiguration" },
### 44 Annuaire
    "ithTphAnnuaire.IRole":                 { 'numero': "441", 'dossier': "44_annuaire" },
    "ithTphAnnuaire.IGroupe":               { 'numero': "442", 'dossier': "44_annuaire" },
    "ithTphAnnuaire.ICategorieCorresp":     { 'numero': "443", 'dossier': "44_annuaire" },
    "ithTphAnnuaire.ICorrespExterne":       { 'numero': "444", 'dossier': "44_annuaire" },
    "ithTphAnnuaire.ICei":                  { 'numero': "445", 'dossier': "44_annuaire" },
    "ithTphAnnuaire.IContactExterneED137":  { 'numero': "446", 'dossier': "44_annuaire" },
    "ithTphAnnuaire.IFOA":                  { 'numero': "447", 'dossier': "44_annuaire" },
### 45 Cahiers de vue
    "ithTphCahiersDeVue.ILoop":             { 'numero': "451", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IPageITH":          { 'numero': "452", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IViewITH":          { 'numero': "453", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IConference":       { 'numero': "454", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IPageTPH":          { 'numero': "455", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IViewTPH":          { 'numero': "456", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IRegleView":        { 'numero': "457", 'dossier': "45_cahiersDeVue" },
    "ithTphCahiersDeVue.IRegleViewDefault": { 'numero': "458", 'dossier': "45_cahiersDeVue" },
### 50 Sites
    "mg2s.Region":                          { 'numero': "501", 'dossier': "50_sites" },
    "mg2s.ISiteCDCSnmp":                    { 'numero': "502", 'dossier': "50_sites" },
    "mg2s.ISiteCDCCie":                     { 'numero': "503", 'dossier': "50_sites" },
    "mg2s.ISiteCERSnmp":                    { 'numero': "504", 'dossier': "50_sites" },
    "mg2s.ISiteCERCie":                     { 'numero': "505", 'dossier': "50_sites" },
    "mg2s.ISiteCOSCASnmp":                  { 'numero': "506", 'dossier': "50_sites" },
    "mg2s.ISiteCOSCACie":                   { 'numero': "507", 'dossier': "50_sites" },
    "mg2s.ISiteCMCCSnmp":                   { 'numero': "508", 'dossier': "50_sites" },
    "mg2s.ISiteCMCCCie":                    { 'numero': "509", 'dossier': "50_sites" },
    "mg2s.ISiteCCSnmp":                     { 'numero': "510", 'dossier': "50_sites" },
    "mg2s.ISiteCCCie":                      { 'numero': "511", 'dossier': "50_sites" },
    "cmoip.ICMoIPDistant":                  { 'numero': "512", 'dossier': "50_sites" },
### 60 Switchs
    "mg2s.ISwitch4507CdcSnmp":          { 'numero': "601", 'dossier': "60_switchs" },
    "mg2s.ISwitch4507Snmp":             { 'numero': "602", 'dossier': "60_switchs" },
    "reseau.IStackOfSwitchSnmp":        { 'numero': "603", 'dossier': "60_switchs" },
    "reseau.ICisco2960X24PortsSnmp":    { 'numero': "604", 'dossier': "60_switchs" },
    "reseau.Cisco2960X24PortsCie":      { 'numero': "605", 'dossier': "60_switchs" },
    "reseau.ICisco2960X48PortsSnmp":    { 'numero': "606", 'dossier': "60_switchs" },
    "reseau.ISwitch48PortsCie":         { 'numero': "607", 'dossier': "60_switchs" },
    "reseau.ICisco365024PortsSnmp":     { 'numero': "608", 'dossier': "60_switchs" },
    "reseau.ICisco365048PortsSnmp":     { 'numero': "609", 'dossier': "60_switchs" },
    "mg2s.IModuleAlimentationSnmp":     { 'numero': "610", 'dossier': "60_switchs" },
    "mg2s.IModuleFibreSnmp":            { 'numero': "611", 'dossier': "60_switchs" },
    "mg2s.IModuleVentilateurSnmp":      { 'numero': "612", 'dossier': "60_switchs" },
    "reseau.IStackOf2SwitchSnmp":       { 'numero': "613", 'dossier': "60_switchs" },
    "reseau.IStackOf2SwitchCie":        { 'numero': "614", 'dossier': "60_switchs" },
    "mg2s.ISwitch4507CdcSnmp":          { 'numero': "6xx", 'dossier': "60_switchs" },
    "mg2s.ISwitch4507Snmp":             { 'numero': "6xx", 'dossier': "60_switchs" },
### 70 Radio
    "mg2s.IChassisSnmp":                        { 'numero': "701", 'dossier': "70_radio" },
    "mg2s.ICarteMcrSnmp":                       { 'numero': "702", 'dossier': "70_radio" },
    "mg2s.IAbstractChassisMcsSnmp":             { 'numero': "703", 'dossier': "70_radio" },
    "mg2s.IAbstractChassisMcsCie":              { 'numero': "704", 'dossier': "70_radio" },
    "mg2s.ICarteChassisCEXSnmp":                { 'numero': "705", 'dossier': "70_radio" },
    "mg2s.ICarteChassisCEXCie":                 { 'numero': "706", 'dossier': "70_radio" },
    "mg2s.ICarteChassisCERSnmp":                { 'numero': "707", 'dossier': "70_radio" },
    "mg2s.ICarteChassisCERCie":                 { 'numero': "708", 'dossier': "70_radio" },
    "mg2s.IPortMcrCommun":                      { 'numero': "709", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsE1Snmp":                   { 'numero': "710", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsE1Cie":                    { 'numero': "711", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsEthSnmp":                  { 'numero': "712", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsEthCie":                   { 'numero': "713", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsPerSnmp":                  { 'numero': "714", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsPerCie":                   { 'numero': "715", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsS0Snmp":                   { 'numero': "716", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsS0Cie":                    { 'numero': "717", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsT2Snmp":                   { 'numero': "718", 'dossier': "70_radio" },
    "mg2s.IPortMcrMcsT2Cie":                    { 'numero': "719", 'dossier': "70_radio" },
### 80 Enregistreurs
    "vgoip.IVgoipEnregistreur":     { 'numero': "801", 'dossier': "80_enregistreurs" },
    "vgoip.IVgoipRejeu":            { 'numero': "802", 'dossier': "80_enregistreurs" },
    "vgoip.IVgoipSimulation":       { 'numero': "803", 'dossier': "80_enregistreurs" },
    "mg2s.IVRoIPClusterSnmp":       { 'numero': "804", 'dossier': "80_enregistreurs" },
    "mg2s.IVRoIPCoteSnmp":          { 'numero': "805", 'dossier': "80_enregistreurs" },
    "mg2s.IVRoIPNoeudSnmp":         { 'numero': "806", 'dossier': "80_enregistreurs" },
    "mg2s.IVRoIPServeurSnmp":       { 'numero': "807", 'dossier': "80_enregistreurs" },
### 90 PERs
    "mg2s.IPerEmetteur":                        { 'numero': "901", 'dossier': "90_pers" },
    "mg2s.IAbstractPerEmetteurCie":             { 'numero': "902", 'dossier': "90_pers" },
    "mg2s.IPerEmetteurRecepteur":               { 'numero': "903", 'dossier': "90_pers" },
    "mg2s.IAbstractPerEmetteurRecepteurCie":    { 'numero': "904", 'dossier': "90_pers" },
    "mg2s.IPerEVFSnmp":                         { 'numero': "905", 'dossier': "90_pers" },
    "mg2s.IPerEVFCie":                          { 'numero': "906", 'dossier': "90_pers" },
    "mg2s.IPerRecepteur":                       { 'numero': "907", 'dossier': "90_pers" },
    "mg2s.IAbstractPerRecepteurCie":            { 'numero': "908", 'dossier': "90_pers" },
### 100 Multiplexeurs
    "mg2s.ICoupleur":                           { 'numero': "1001", 'dossier': "100_multiplexeurs" },
    "mg2s.ICoupleurCie":                        { 'numero': "1002", 'dossier': "100_multiplexeurs" },
### 110 Supervision
    "cmoip.ICmoipClient":                   { 'numero': "1101", 'dossier': "110_supervision" },
    "cmoip.ICmoipClientCie":                { 'numero': "1102", 'dossier': "110_supervision" },
    "cmoip.ICmoipSnmp":                     { 'numero': "1103", 'dossier': "110_supervision" },
    "cmoip.ICmoipCie":                      { 'numero': "1104", 'dossier': "110_supervision" },
    "cmoip.ICmoipServerStandaloneSnmp":     { 'numero': "1105", 'dossier': "110_supervision" },
    "cmoip.ICmoipServerStandaloneCie":      { 'numero': "1106", 'dossier': "110_supervision" },
### 120 Routeur
    "mg2s.IRouteur":                    { 'numero': "1201", 'dossier': "120_routeur" },
    "mg2s.IRouteurCie":                 { 'numero': "1202", 'dossier': "120_routeur" },
### 130 Gestion de ressources
    "mg2s.IFarCexSnmp":                 { 'numero': "1301", 'dossier': "130_GestionDeRessources" },
    "mg2s.IFarCexCie":                  { 'numero': "1302", 'dossier': "130_GestionDeRessources" },
    "mg2s.IFarCerSnmp":                 { 'numero': "1303", 'dossier': "130_GestionDeRessources" },
    "mg2s.IFarCerCie":                  { 'numero': "1304", 'dossier': "130_GestionDeRessources" },
    "mil.IARoIPLogiqueSnmp":            { 'numero': "1305", 'dossier': "130_GestionDeRessources" },
    "mg2s.IARoIPLogiqueCie":            { 'numero': "13051", 'dossier': "130_GestionDeRessources" },       # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerAnalogiqueMilitaireCie":   { 'numero': "130x", 'dossier': "130_GestionDeRessources" },        # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerAnalogiqueMilitaireSnmp":  { 'numero': "130x", 'dossier': "130_GestionDeRessources" },        # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerEd137MilitaireCie":        { 'numero': "130x", 'dossier': "130_GestionDeRessources" },        # !!!!!!! numéro ?? !!!!!!!!
    "mil.IPerEd137MilitaireSnmp":       { 'numero': "130x", 'dossier': "130_GestionDeRessources" },        # !!!!!!! numéro ?? !!!!!!!!
### 140 Serveurs
    "serveurs.IClusterUCGenerique":         { 'numero': "1401", 'dossier': "140_serveurs" },
    "serveurs.IClusterUCGeneriquePIU":      { 'numero': "1401", 'dossier': "140_serveurs" },
    "serveurs.IServeurSeducs":              { 'numero': "1402", 'dossier': "140_serveurs" },
    "serveurs.IServeurUCGeneriqueSnmp":     { 'numero': "1403", 'dossier': "140_serveurs" },
    "serveurs.IServeurUCGeneriquePIUSnmp":  { 'numero': "1403", 'dossier': "140_serveurs" },
    "serveurs.IServeurUCGeneriqueCie":      { 'numero': "1404", 'dossier': "140_serveurs" },
### 150 Parefeu
    "mg2s.IClusterDeNetasqSnmp":        { 'numero': "1501", 'dossier': "150_parefeu" },
    "mg2s.IClusterDeNetasqCie":         { 'numero': "1502", 'dossier': "150_parefeu" },
    "mg2s.IChiffreurHorsClusterSnmp":   { 'numero': "1503", 'dossier': "150_parefeu" },
    "mg2s.IChiffreurHorsClusterCie":    { 'numero': "1504", 'dossier': "150_parefeu" },
    "mg2s.ILiaisonVpnSnmp":             { 'numero': "1505", 'dossier': "150_parefeu" },
    "mg2s.ILiaisonVpnCie":              { 'numero': "1506", 'dossier': "150_parefeu" },
### 160 Collecteur alarmes
    "mg2s.IPeripheriqueCAMaitreSnmp":       { 'numero': "1601", 'dossier': "160_collecteurAlarmes" },
    "mg2s.IPeripheriqueCAMaitreCie":        { 'numero': "1602", 'dossier': "160_collecteurAlarmes" },
    "mg2s.IPeripheriqueCAEsclaveSnmp":      { 'numero': "1603", 'dossier': "160_collecteurAlarmes" },
    "mg2s.IPeripheriqueCAEsclaveCie":       { 'numero': "1604", 'dossier': "160_collecteurAlarmes" },
    "mg2s.IBoucleCASnmp":                   { 'numero': "1605", 'dossier': "160_collecteurAlarmes" },
    "mg2s.IBoucleCACie":                    { 'numero': "1606", 'dossier': "160_collecteurAlarmes" },
    "collecteur.alarmes.IOptoCie":          { 'numero': "1607", 'dossier': "160_collecteurAlarmes" },
    "collecteur.alarmes.IBoucleOptoCie":    { 'numero': "1608", 'dossier': "160_collecteurAlarmes" },
### 170 Atelier Energie
    "mg2s.IAtelierEnergie":         { 'numero': "1701", 'dossier': "170_atelierEnergie" },
    "mg2s.IAtelierEnergieCie":      { 'numero': "1702", 'dossier': "170_atelierEnergie" },
    "mg2s.IAtelierEnergieV7":       { 'numero': "1703", 'dossier': "170_atelierEnergie" },
    "mg2s.IAtelierEnergieV7Cie":    { 'numero': "1704", 'dossier': "170_atelierEnergie" },
### 180 Protections
    "mg2s.ICabine":             { 'numero': "1801", 'dossier': "180_protections" },
    "mg2s.ILocalSnmp":          { 'numero': "1802", 'dossier': "180_protections" },
    "mg2s.ILocalCie":           { 'numero': "1803", 'dossier': "180_protections" },
    "mg2s.IBaieSnmp":           { 'numero': "1804", 'dossier': "180_protections" },
    "mg2s.IBaieCie":            { 'numero': "1805", 'dossier': "180_protections" },
### 190 Liens
    "port.ILienEth":                { 'numero': "1901", 'dossier': "190_liens" },
    "port.ILienEthCie":             { 'numero': "1902", 'dossier': "190_liens" },
### 200 Opto bic
    "collecteur.alarmes.IOptoSnmp":         { 'numero': "2001", 'dossier': "200_optoBic" },
    "collecteur.alarmes.IBoucleOptoSnmp":   { 'numero': "2002", 'dossier': "200_optoBic" },
### 230 VSoIP
    "mil.IVSoIP":               { 'numero': "2301", 'dossier': "230_VSoIP" },
    "mg2s.IVSoIPCie":           { 'numero': "23011", 'dossier': "230_VSoIP" },

### 240 PXoIP
    "mil.IPXoIPLogiqueSnmp":    { 'numero': "240", 'dossier': "240_PXoIP" },
    "mg2s.IPXoIPLogiqueCie":    { 'numero': "2401", 'dossier': "240_PXoIP" },
### 250 POoIP
    "mil.IPOoIPLogiqueSnmp":        { 'numero': "250", 'dossier': "250_POoIP" },
    "mil.IPOoIPContainer":          { 'numero': "251", 'dossier': "250_POoIP" },
    "mg2s.IPOoIPLogiqueCie":        { 'numero': "2501", 'dossier': "250_POoIP" },
    "mil.IPOoIPContainerSnmp":      { 'numero': "2511", 'dossier': "250_POoIP" },
### 260 VGoIP
    "mg2s.IChassisVGoIPCie":            { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mg2s.IChassisVGoIPSnmp":           { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mil.IMCRVGoIPCie":                 { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mil.IMCRVGoIPSnmp":                { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mil.IMiaeVGoIPCie":                { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mil.IMiaeVGoIPSnmp":               { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mg2s.IVGoIPDacCie":                { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mil.IVGoIPDacSnmp":                { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mg2s.IVGoIPServeurLogiqueCie":     { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
    "mil.IVGoIPServeurLogiqueSnmp":     { 'numero': "260x", 'dossier': "260_VGoIP" },     # !! numéro ?? !!
### 300 Silencieux
    "supervision.ISilencieuxCer":       { 'numero': "3001", 'dossier': "300_silencieux" },
    "supervision.ISilencieuxCdcCie":    { 'numero': "3002", 'dossier': "300_silencieux" },
### 310 Sécurité
    "securite.ICertificat":                     { 'numero': "3101", 'dossier': "310_securite" },
    "securite.ICertificatCIE":                  { 'numero': "3102", 'dossier': "310_securite" },
    "securite.ICertificatPFC":                  { 'numero': "3103", 'dossier': "310_securite" },
    "securite.ICertificatRevocationList":       { 'numero': "3104", 'dossier': "310_securite" },
    "securite.ICertificatRevocationListCIE":    { 'numero': "3105", 'dossier': "310_securite" },
    "securite.ICertificatRevocationListPFC":    { 'numero': "3106", 'dossier': "310_securite" },
    "securite.IIntegrityChecker":               { 'numero': "3107", 'dossier': "310_securite" },
    "securite.IIntegrityCheckerCIE":            { 'numero': "3108", 'dossier': "310_securite" },
    "securite.IVirusChecker":                   { 'numero': "3109", 'dossier': "310_securite" },
    "securite.IVirusCheckerCIE":                { 'numero': "3110", 'dossier': "310_securite" },
### 320 Autres
    "mil.IObjetDeSynthese":                 { 'numero': "3201", 'dossier': "320_autres" },
    "mil.IAdpsServer":                      { 'numero': "3202", 'dossier': "320_autres" },
    "mil.IPingSupervisedObject":            { 'numero': "3203", 'dossier': "320_autres" },
    "mil.IAdpsSupervisedObject":            { 'numero': "3204", 'dossier': "320_autres" },     # à vérifier
    "mg2s.IEquipementNonGere":              { 'numero': "3205", 'dossier': "320_autres" },
    "system.IHttpServeur":                  { 'numero': "3206", 'dossier': "320_autres" },
    "system.IPodmanContainer":              { 'numero': "3208", 'dossier': "320_autres" },
    "mil.IInstanceApplicationMetierSnmp":   { 'numero': "3210", 'dossier': "320_autres" },     # !! 32010 ?? !!
    "mil.IHttpServeurMilitaire":            { 'numero': "32061", 'dossier': "320_autres" },
    "mil.IPodmanPodMilitaire":              { 'numero': "32071", 'dossier': "320_autres" },
### 330 Configuration externe
    "mg2s.IConfigExterne":                  { 'numero': "3301", 'dossier': "330_configurationExterne" },
    "mg2s.ISiteConfigExterne":              { 'numero': "3302", 'dossier': "330_configurationExterne" },
    "mg2s.IZoneConfigExterne":              { 'numero': "3303", 'dossier': "330_configurationExterne" },
### 340 Voies
    "supervision.IVoieRadioSnmp":           { 'numero': "3401", 'dossier': "340_voies" },
    "supervision.IVoieRadioCie":            { 'numero': "3402", 'dossier': "340_voies" },
    "supervision.IVoieCentreCorrelee":      { 'numero': "3403", 'dossier': "340_voies" },
    "supervision.IVoieCentreSnmp":          { 'numero': "3404", 'dossier': "340_voies" },
    "supervision.IVoieCentreCie":           { 'numero': "3405", 'dossier': "340_voies" },
    "supervision.IVoieCentreParVoieRadio":  { 'numero': "3406", 'dossier': "340_voies" },
    "supervision.IMission":                 { 'numero': "3407", 'dossier': "340_voies" },
    "supervision.IMissionCOSCA":            { 'numero': "3408", 'dossier': "340_voies" },
### 360 RDO-Configuration
    "rdoConfiguration.ICategorieVoie":          { 'numero': "3601", 'dossier': "360_rdoConfiguration" },
    "rdoConfiguration.IEQF":                    { 'numero': "3602", 'dossier': "360_rdoConfiguration" },
    "rdoConfiguration.IPageTOV":                { 'numero': "3604", 'dossier': "360_rdoConfiguration" },
    "rdoConfiguration.IParametresGenerauxRDO":  { 'numero': "3605", 'dossier': "360_rdoConfiguration" },
    "rdoConfiguration.IProfilRadioMg2s":        { 'numero': "3603", 'dossier': "360_rdoConfiguration" },
### 
### 
    "site.IVoieParCentre": { 'numero': "xxx", 'dossier': "" },

    "FIN": { 'numero': "999999999", 'dossier': "" }
}
