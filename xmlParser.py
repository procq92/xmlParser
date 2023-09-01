import xml
import xml.etree.ElementTree as et
from pathlib import Path
#import xml.etree.ElementTree.tostring as ts
from pprint import pprint
import argparse
import logging, time

classes_a_exclure = ("cmoip.ICMoIPDistant",
                    "cmoip.ICmoipCie",
                    "cmoip.ICmoipClient",
                    "cmoip.ICmoipClientCie",
                    "cmoip.ICmoipServerStandaloneCie",
                    "cmoip.ICmoipServerStandaloneSnmp",
                    "cmoip.ICmoipSnmp",
                    "ithTphAnnuaire.ICorrespExterne",
                    "mg2s.IAtelierEnergie",
                    "mg2s.IAtelierEnergieCie",
                    "mg2s.IAtelierEnergie"
                    "mg2s.IAtelierEnergieCie",
                    "mg2s.IFarCerCie"
                    "mg2s.IFarCerSnmp"
                    "mg2s.IFarCexCie"
                    "mg2s.IFarCexSnmp"
                    )

numeros_de_classe = {
    "cmoip.ICMoIPDistant":                  "",
    "cmoip.ICmoipCie":                      "1104",
    "cmoip.ICmoipClient":                   "1101",
    "cmoip.ICmoipClientCie":                "1102",
    "cmoip.ICmoipServerStandaloneCie":      "1106",
    "cmoip.ICmoipServerStandaloneSnmp":     "1105",
    "cmoip.ICmoipSnmp":                     "1103",

    "collecteur.alarmes.IBoucleOptoCie":    "",
    "collecteur.alarmes.IBoucleOptoSnmp":   "",
    "collecteur.alarmes.IOptoCie":          "",
    "collecteur.alarmes.IOptoSnmp":         "",

    "ithTphAnnuaire.ICategorieCorresp":     "443",
    "ithTphAnnuaire.ICei":                  "445",
    "ithTphAnnuaire.IContactExterneED137":  "446",
    "ithTphAnnuaire.ICorrespExterne":       "444",
    "ithTphAnnuaire.IGroupe":               "442",
    "ithTphAnnuaire.IRole":                 "441",
    "ithTphAnnuaire.ITelProfil":            "",

    "ithTphCahiersDeVue.IConference":       "454",
    "ithTphCahiersDeVue.ILoop":             "451",
    "ithTphCahiersDeVue.IPageITH":          "452",
    "ithTphCahiersDeVue.IPageTPH":          "455",
    "ithTphCahiersDeVue.IRegleView":        "457",
    "ithTphCahiersDeVue.IRegleViewDefault": "458",
    "ithTphCahiersDeVue.IViewITH":          "453",
    "ithTphCahiersDeVue.IViewTPH":          "456",

    "ithTphConfiguration.IConferenceMeetMe":    "438",
    "ithTphConfiguration.IDomains":             "437",
    "ithTphConfiguration.IFaisceau":            "439",
    "ithTphConfiguration.IGfu":                 "432",
    "ithTphConfiguration.IGfuIndex":            "431",
    "ithTphConfiguration.IParamGenTph":         "433",
    "ithTphConfiguration.IPlanNumerotation":    "434",
    "ithTphConfiguration.IRestrictionsAppels":  "435",
    "ithTphConfiguration.IPrioritySettings":    "430",

    "ithTphEquipements.ITsoip":                     "401",
    "ithTphEquipements.ITsoipServerStandalone":     "402",
    "ithTphEquipements.ITsoipServerStandaloneCie":  "403",

    "mg2s.IAtelierEnergie":         "1701",
    "mg2s.IAtelierEnergieCie":      "1702",
    "mg2s.IAtelierEnergieV7":       "1703",
    "mg2s.IAtelierEnergieV7Cie":    "1704",

    "mg2s.IBaieCie": "",
    "mg2s.IBaieSnmp": "",

    "mg2s.IBoucleCACie": "",
    "mg2s.IBoucleCASnmp": "",

    "mg2s.ICabine": "",

    "mg2s.IAbstractChassisMcsCie":              "704",
    "mg2s.IAbstractChassisMcsSnmp":             "703",
    "mg2s.ICarteChassisCERCie":                 "708",
    "mg2s.ICarteChassisCERSnmp":                "707",
    "mg2s.ICarteChassisCEXCie":                 "706",
    "mg2s.ICarteChassisCEXSnmp":                "705",
    "mg2s.ICarteMcrSnmp":                       "",
    "mg2s.IChassisSnmp":                        "",

    "mg2s.IChiffreurHorsClusterCie":    "1504",
    "mg2s.IChiffreurHorsClusterSnmp":   "1503",
    "mg2s.IClusterDeNetasqCie":         "1502",
    "mg2s.IClusterDeNetasqSnmp":        "1501",

    "mg2s.IConfigExterne":      "3301",
    "mg2s.ISiteConfigExterne":  "3302",
    "mg2s.IZoneConfigExterne":  "3303",

    "mg2s.ICoupleur":       "1001",
    "mg2s.ICoupleurCie":    "1002",

    "mg2s.IEquipementNonGere": "",

    "mg2s.IFarCerCie":      "1304",
    "mg2s.IFarCerSnmp":     "1303",
    "mg2s.IFarCexCie":      "1302",
    "mg2s.IFarCexSnmp":     "1301",

    "mg2s.ILiaisonVpnCie": "",
    "mg2s.ILiaisonVpnSnmp": "",

    "mg2s.ILocalCie": "",
    "mg2s.ILocalSnmp": "",

    "mg2s.IModuleAlimentationSnmp":     "610",
    "mg2s.IModuleFibreSnmp":            "611",
    "mg2s.IModuleVentilateurSnmp":      "612",

    "mg2s.IPerEVFCie":                          "906",
    "mg2s.IPerEVFSnmp":                         "905",
    "mg2s.IPerEmetteur":                        "901",
    "mg2s.IPerEmetteurRecepteur":               "903",
    "mg2s.IPerRecepteur":                       "907",
    "mg2s.IAbstractPerEmetteurCie":             "902",
    "mg2s.IAbstractPerEmetteurRecepteurCie":    "904",
    "mg2s.IAbstractPerRecepteurCie":            "908",

    "mg2s.IPeripheriqueCAEsclaveCie": "",
    "mg2s.IPeripheriqueCAEsclaveSnmp": "",
    "mg2s.IPeripheriqueCAMaitreCie": "",
    "mg2s.IPeripheriqueCAMaitreSnmp": "",

    "mg2s.IPortMcrCommun":      "709",
    "mg2s.IPortMcrMcsE1Cie":    "711",
    "mg2s.IPortMcrMcsE1Snmp":   "710",
    "mg2s.IPortMcrMcsEthCie":   "713",
    "mg2s.IPortMcrMcsEthSnmp":  "712",
    "mg2s.IPortMcrMcsPerCie":   "715",
    "mg2s.IPortMcrMcsPerSnmp":  "714",
    "mg2s.IPortMcrMcsS0Cie":    "717",
    "mg2s.IPortMcrMcsS0Snmp":   "716",
    "mg2s.IPortMcrMcsT2Cie":    "719",
    "mg2s.IPortMcrMcsT2Snmp":   "718",

    "mg2s.IRouteur":        "1201",
    "mg2s.IRouteurCie":     "1202",

    "mg2s.Region":              "501",
    "mg2s.ISiteCCCie":          "511",
    "mg2s.ISiteCCSnmp":         "510",
    "mg2s.ISiteCDCCie":         "503",
    "mg2s.ISiteCDCSnmp":        "502",
    "mg2s.ISiteCERCie":         "505",
    "mg2s.ISiteCERSnmp":        "504",
    "mg2s.ISiteCMCCCie":        "509",
    "mg2s.ISiteCMCCSnmp":       "508",
    "mg2s.ISiteCOSCACie":       "507",
    "mg2s.ISiteCOSCASnmp":      "506",


    "mg2s.ISitePIUCie":             "12",   # de la catégorie 1) Configuration (CMoIP)

    "mg2s.ISwitch4507CdcSnmp": "",
    "mg2s.ISwitch4507Snmp": "",

    "mg2s.IVRoIPClusterSnmp":   "804",
    "mg2s.IVRoIPCoteSnmp":      "805",
    "mg2s.IVRoIPNoeudSnmp":     "806",
    "mg2s.IVRoIPServeurSnmp":   "807",


    "mil.IAdpsServer":              "3202",
    "mil.IAdpsSupervisedObject":    "3204",     # à vérifier
    "mil.IObjetDeSynthese":         "3201",
    "mil.IPingSupervisedObject":    "3203",

    "pocConfiguration.IDSCPSettings":               "413",
    "pocConfiguration.IEnregIpTsoipSettingsConf":   "415",
    "pocConfiguration.ILevelsTsoip":                "414",
    "pocConfiguration.IMission":                    "416",
    "pocConfiguration.IParametresGeneraux":         "411",

    "pocEquipement.IAudioProfiles":             "422",
    "pocEquipement.IVPoIP":                     "421",

    "port.ILienEth":                "1901",
    "port.ILienEthCie":             "1902",

    "rdoConfiguration.ICategorieVoie":          "3601",
    "rdoConfiguration.IEQF":                    "3602",
    "rdoConfiguration.IPageTOV":                "3604",
    "rdoConfiguration.IParametresGenerauxRDO":  "3605",
    "rdoConfiguration.IProfilRadioMg2s":        "3603",

    "reseau.Cisco2960X24PortsCie":      "",
    "reseau.ICisco2960X24PortsSnmp":    "",
    "reseau.ICisco2960X48PortsSnmp":    "",
    "reseau.ICisco365024PortsSnmp":     "608",
    "reseau.ICisco365048PortsSnmp":     "609",
    "reseau.IStackOf2SwitchCie":        "614",
    "reseau.IStackOf2SwitchSnmp":       "613",
    "reseau.IStackOfSwitchSnmp":        "",
    "reseau.ISwitch48PortsCie":         "",

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

    "serveurs.IClusterUCGenerique":         "1401",
    "serveurs.IClusterUCGeneriquePIU":      "1401",
    "serveurs.IServeurSeducs":              "1402",
    "serveurs.IServeurUCGeneriqueCie":      "1404",
    "serveurs.IServeurUCGeneriquePIUSnmp":  "1403",
    "serveurs.IServeurUCGeneriqueSnmp":     "1403",

    "site.IVoieParCentre": "",

    "srsa.edcdc.IPlanRemplacement":             "0312",
    "srsa.edcdc.IPlanRemplacementAActiver":     "0313",
    "srsa.edcdc.shared.ICvr":                   "0300",
    "srsa.edcdc.shared.IEqfFixe":               "0305",
    "srsa.edcdc.shared.IFrequence":             "0304",
    "srsa.edcdc.shared.IGroupeUtilisateurCdc":  "0311",
    "srsa.edcdc.shared.IPageTov":               "0302",
    "srsa.edcdc.shared.IProfilRepli":           "0310",
    "srsa.edcdc.shared.IProfilUtilisateur":     "0309",
    "srsa.edcdc.shared.IToc":                   "0301",
    "srsa.edcdc.shared.IVoiePermanente":        "0306",
    "srsa.edcdc.shared.IZoneTravail":           "0303",

    "supervision.ISilencieuxCdcCie":    "3002",
    "supervision.ISilencieuxCer":       "3001",

    "supervision.IVoieCentreCie":           "3405",
    "supervision.IVoieCentreCorrelee":      "3403",
    "supervision.IVoieCentreParVoieRadio":  "",
    "supervision.IVoieCentreSnmp":          "3404",
    "supervision.IVoieRadioCie":            "3402",
    "supervision.IVoieRadioSnmp":           "3401",
    "supervision.IMission":                 "3407",
    "supervision.IMissionCOSCA":            "3408",

    "system.IOperatingStateAbnormalStatusConfiguration":    "11",
    "system.piu.IVersionAntiVirusCie":                      "14",
    "system.piu.IVersionAntiVirusSnmp":                     "13",
    "system.piu.IVersionElementSecretCie":                  "15", # vérifier le numéro
    "system.piu.IVersionElementSecretSnmp":                 "16", # vérifier le numéro
    "system.piu.IVersionSystemeCie":                        "18",
    "system.piu.IVersionSystemeSnmp":                       "17",
    "system.piu.IVersionTorrentCie":                        "19",

    "vgoip.IVgoipEnregistreur":     "801",
    "vgoip.IVgoipRejeu":            "802",
    "vgoip.IVgoipSimulation":       "803",

    "FIN": "999999999"
}

def decrireNoeud(noeud, niveau=0, decrireEnfants=False):
    print("N=", niveau, "   tag=", noeud.tag, "attrib=", noeud.attrib, "len=", len(noeud))
    if len(noeud) > 0 and decrireEnfants:
        for noeudEnfant in noeud:
            decrireNoeud(noeudEnfant, niveau + 1)

def decrireEnfants(noeud):
    if len(noeud) > 0:
        index = 0
        for noeudEnfant in noeud:
            print(index, "tag=", noeudEnfant.tag, "id=", noeudEnfant.attrib.get('class-name', ""))
            #xml.etree.ElementTree.tostring(noeudEnfant)
            index+= 1
        print(dir(noeudEnfant[0]))
        tt = xml.etree.ElementTree.tostring(noeudEnfant[0])
        print(f"===== tt={tt}")

gmTime = time.gmtime()
dateTexte = f"{gmTime.tm_year}-{gmTime.tm_mon:02d}-{gmTime.tm_mday:02d} {gmTime.tm_hour:02d}:{gmTime.tm_min:02d}:{gmTime.tm_sec:02d}"

p = Path.cwd()

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='ajoute des traces', action='store_true')
parser.add_argument('filename', help='nom du fichier xml à parser')
#parser.add_argument('resultFolder', default='templ', help='répertoire où placer les templates')
args = parser.parse_args()
# if args.resultFolder:
#     resultFolder = args.resultFolder
# else:
#     resultFolder = "templ"
print("filename=" + args.filename)
#print("resultFolder=" + args.resultFolder)
#print("aaaaaaaaaaa")
resultFolder = p / (args.filename + "_templParClasse")
listeClasses =  p / (args.filename + "_listeClasses.txt")
listeClassesExclues =  p / (args.filename + "_listeClassesExclues.txt")
listeClassesInclues =  p / (args.filename + "_listeClassesInclues.txt")
if not resultFolder.exists():
    resultFolder.mkdir()
    print(f"Création du dossier {resultFolder.name}")
if resultFolder.is_file():
    logging.error(f"Le répertoire de destination est un fichier, et pas un répertoire")
    exit(1)
if not listeClasses.exists():
    listeClasses.touch()
if not listeClassesExclues.exists():
    listeClassesExclues.touch()
if not listeClassesInclues.exists():
    listeClassesInclues.touch()
tree = et.parse(args.filename)
root = tree.getroot()

texte_description = f"<!-- date : {dateTexte} -->\n<!-- dossier : {p} -->\n<!-- squelette : {args.filename} -->\n<!-- sw_cmoip_version : {root.attrib.get('sw_cmoip_version', '?????')} -->\n"
print("texte_description=" + texte_description)

# print(type(p))
# print(p)
# print(type(resultFolder))
groupObjectModel = root[0][0]
texteListeClasses = ""
texteListeClassesInclues = ""
texteListeClassesExclues = ""
nbClasses = 0
nbClassesExclues = 0
nbClassesInclues = 0
for enfant in groupObjectModel:
    class_name = enfant.get('class-name')
    nbClasses += 1
    texteListeClasses += "\n" + class_name
    if class_name in classes_a_exclure:
        nbClassesExclues += 1
        texteListeClassesExclues += "\n" + class_name
    else:
        nbClassesInclues += 1
        #print (class_name)
        #if class_name == "ithTphConfiguration.IDomains":
        #    print (enfant)
        numero_classe = numeros_de_classe.get(class_name)
        if numero_classe:
            if numero_classe == "":
                texte_numero = "na"
            else:
                texte_numero = f"{numero_classe}"
        else:
            texte_numero = "null"
        texte_fichier =  f'<!-- fichier : {"templ_" + texte_numero + class_name + ".xml"} -->\n'
        texte_classe = f'<!-- classe : {texte_numero + " === " + class_name} -->\n\n'
        texteListeClassesInclues += "\n" + class_name
        filename = resultFolder / ("templ_" + texte_numero + "_" + class_name + ".xml")
        #print(f"======  {filename.name} {filename.stem} {filename.suffix} {filename.parts}")
        enfant_str = xml.etree.ElementTree.tostring(enfant, encoding='unicode')
        filename.write_text(texte_description + texte_fichier + texte_classe + enfant_str, encoding='utf-8')
        # with open(filename, "w", encoding="utf-8") as f:
        #     f.write(xml.etree.ElementTree.tostring(enfant, encoding='unicode'))
listeClasses.write_text(texteListeClasses)
listeClassesInclues.write_text(texteListeClassesInclues)
listeClassesExclues.write_text(texteListeClassesExclues)
print(f"{nbClasses} classes trouvées")
print(f"{nbClassesInclues} classes inclues")
print(f"{nbClassesExclues} classes exclues")

if False:
    print("-----------------------------")
    #decrireNoeud(root, 0, True)
    groupObjectModel = root[0][0]
    decrireEnfants(groupObjectModel)
    print("decrireNoeud(groupObjectModel[4])")
    decrireNoeud(groupObjectModel[4])
    print("------ xml -------")
    print(dir(xml))

    print("------ xml.etree -------")
    print(dir(xml.etree))

    print("------ xml.etree.ElementTree -------")
    print(dir(xml.etree.ElementTree))

    print("=== decrireNoeud(groupObjectModel) ===")
    decrireNoeud(groupObjectModel)
    print("=== decrireEnfants(groupObjectModel) ===")
    decrireEnfants(groupObjectModel)

    print("=== decrireNoeud(groupObjectModel[12],decrireEnfants=True) ===")
    decrireNoeud(groupObjectModel[12],decrireEnfants=True)
    tt = xml.etree.ElementTree.tostring(groupObjectModel[12], encoding='unicode')
    #print("=== tt ===")
    print(tt)
    with open ('testTemplate.xml', "wt", encoding="utf-8") as out:
        pprint(tt, width=120, stream=out)

    print("=== fin ===")
#decrireNoeud(object)
#print(f"+++class-name={object.attrib.get('class-name', '')}")
#tt = xml.etree.ElementTree.tostring(groupObjectModel[5])
#print(tt)