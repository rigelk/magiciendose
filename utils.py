from centre.models import CentreAmbulatoire
from vaccin.models import Vaccin
from cles_region.models import ClesRegion
from cles_departement.models import ClesDepartement
from doses.models import DosesRegion, DosesDepartement, DosesCentre

import pandas
import numpy as np


def get_cva():
    df = pandas.read_excel("data/Referentiel_centres_vacci_20210421.xlsx")
    df.drop(df[~df.TYPOLOGIE.isin({'CVA', 'CV MIXTE'})].index, axis=0, inplace=True)
    df['Code'] = [str(e).zfill(5) for e in df.com_insee]
    return df


def peuple_centres():
    """
    Peupler la table CentreAmbulatoire

    :return:
    """
    df = get_cva()
    for _, el in df.iterrows():
        centre = CentreAmbulatoire(nom=el.nom, gid=el.gid, code_postal=el.com_cp,
                                   code_commune_insee=el.com_insee,
                                   capacite=np.random.randint(1000))
        centre.save()

    return


def peuple_vaccins():
    """
    Peupler la table Vaccin
    :return:
    """
    pfizer = Vaccin(nom="Pfizer", intervalle_injections=42)
    pfizer.save()
    moderna = Vaccin(nom="Moderna", intervalle_injections=28)
    moderna.save()
    az = Vaccin(nom="AstraZeneca", intervalle_injections=28)
    az.save()


def peuple_regions():
    """
    Peupler les regions et les departements pour l'IDF
    :return:
    """
    for semaine in range(10, 22):
        region_semaine = ClesRegion(semaine_de_vaccination=semaine, numero_region=6)
        region_semaine.save()
        # Bon c'est un hack
        for dept in [76, 78, 79, 92, 93, 94, 95, 96]:
            dept_semaine = ClesDepartement(semaine_de_vaccination=semaine, numero_departement=dept,
                                           code_postal=str(dept - 1).ljust(5, '0'))
            dept_semaine.save()

    return
